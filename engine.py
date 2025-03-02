import asyncio
from enum import Enum
import copy
import traceback

from PySide6 import QtCore
import numpy as np
import quantiphy as q
from pydatacq import LiveSDS

from fft_calculations import V_to_Vrms, Vrms_to_dBVrms, fft, thd

from sdg import SDG
from pydatacq.sds import vdiv_lookup


# The flag which tells the THD process to cancel
# as soon as possible.
_cancelSweep: bool = False

# The event which is set if the sweep has finished.
_eventRunFinished: asyncio.Event

f0_ = []
thd_ = []
ampl_ = []

# Number of periods from which to calculate THD
periods = 25

# Number of waveforms to skip before taking measurements
_numberToSkip = 5


# Global event which denotes that for the
# current frequecy (in sweep mode) a THD
# value has been collected.
_eventSampled: asyncio.Event = None


# Signal generator keys
keySDGUse = "sdgUse"
keySDGChannel = "sdgChannel"
keySDGMode = "sdgMode"
keySDGCWAmplitude = "sdgCWAmplitude"
keySDGFixSweep = "sdgFixSweep"
keySDGAMFrequency = "sdgAMFrequency"
keySDGAMAmplitude = "sdgAMAmplitude"
keySDGAMModulationDepth = "sdgAMModulationDepth"
keySDGFMFrequency = "sdgFMFrequency"
keySDGFMAmplitude = "sdgFMAmplitude"
keySDGFMFrequencyDeviation = "sdgFMFreuencyDeviation"
keySDGFixedF0 = "sdgFixed_f0"
keySDGSweepMinFreq = "sdgSweep_minFreq"
keySDGSweepMaxFreq = "sdgSweep_maxFreq"
keySDGSweepStep = "sdgSweepStep"

# Oscilloscope keys
keySDSChannel = "sdsChannel"
keySDSAutoVertical = "sdsAutoVertical"
keySDSAutoTimebase = "sdsAutoTimebase"
keySDSPeriods = "sdsPeriods"

# FFT keys
keyFFTPlotMinY = "thdMinY"
keyFFTPlotMaxY = "thdMaxY"

# THD keys
keyTHDFloor = "thdFloor"
keyTHDHarmonics = "thdHarmonics"
keyTHDMaxFrequency = "thdMaxFrequency"
keyTHDf0 = "thdF0"
keyTHDAverage = "thdAverage"
keyTHDPlotAmplitude = "thdPlotAmplitude"


class SDGMode(Enum):
    CW = 0
    AM = 1
    FM = 2


class SDGFixSweep(Enum):
    FIX = 0
    SWEEP = 1


# Holds the currently active parameters
# This serves as the defaults as well.
active = {
    keySDGUse: True,
    keySDGChannel: 1,
    keySDGMode: SDGMode.CW,
    keySDGCWAmplitude: 1,
    keySDGFixSweep: SDGFixSweep.FIX,
    keySDGAMFrequency: "1M",
    keySDGAMAmplitude: 1,
    keySDGAMModulationDepth: 50,    
    keySDGFMFrequency: "10.7M",
    keySDGFMAmplitude: "1",
    keySDGFMFrequencyDeviation: "75k",
    keySDGFixedF0: "1k",
    keySDGSweepMinFreq: "1k",
    keySDGSweepMaxFreq: "10k",
    keySDGSweepStep: "500",
    
    keySDSChannel: "1",
    keySDSAutoVertical: False,
    keySDSAutoTimebase: True,
    keySDSPeriods: 50,
    
    keyTHDHarmonics: "5",
    keyTHDFloor: "-80",
    keyTHDAverage: "4",

    keyFFTPlotMinY: "-100",
    keyFFTPlotMaxY: "0",

    keyTHDPlotAmplitude: True,
}


mainWindow = None

live_sds = None
sdg: SDG = None
sdgMode: SDGMode = None


def qCheckState2Bool(s):
    return s == QtCore.Qt.CheckState.Checked


sdgIP = ""
sdgPort = 5025
sdgUseVisa = True
sdgQueryDelay = 0.5
sdsIP = ""
sdsPort = 5025


#
def sdgUseSDG():
    return active[keySDGUse]


#
def sdgCWAmplitude():
    return active[keySDGCWAmplitude]


#
def sdgChannel():
    return active[keySDGChannel]


#
def sdgAMFrequency():
    return active[keySDGAMFrequency]


#
def SDGAMAmplitude():
    return active[keySDGAMAmplitude]


#
def SDGAMModulationDepth():
    return active[keySDGAMModulationDepth]


#
def SDGFMFrequency():
    return active[keySDGFMFrequency]


#
def SDGFMAmplitude():
    return active[keySDGFMAmplitude]


#
def SDGFMFrequencyDeviation():
    return active[keySDGFMFrequencyDeviation]


#
def SDGFixedF0():
    return active[keySDGFixedF0]


#
def SDGSweepMinimumFrequency():
    return active[keySDGSweepMinFreq]


#
def SDGSweepMaximumFrequency():
    return active[keySDGSweepMaxFreq]


#
def SDGSweepStep():
    return active[keySDGSweepStep]


#
def oscChannel():
    return active[keySDSChannel]


#
def sdsAutoAdjustVertical():
    return active[keySDSAutoVertical]


#
def sdsAutoAdjustTimebase():
    return active[keySDSAutoTimebase]


#
def sdsPeriods():
    return active[keySDSPeriods]


#
def thdF0():
    return active[keyTHDf0]


#
def thdHarmonics():
    return active[keyTHDHarmonics]


#
def thdFloor():
    return active[keyTHDFloor]


#
def plotMinY():
    return active[keyFFTPlotMinY]


#
def plotMaxY():
    return active[keyFFTPlotMaxY]


#
def thdAverage():
    return active[keyTHDAverage]


#
def thdPlotAmplitude():
    return active[keyTHDPlotAmplitude]


#
def dbVrms_to_dBV(x):
    return x + 3.01


#
def log(txt):
    mainWindow.print(txt + "\n")


_skip = 0
_doSample = False
_sweepSamples = 0
_sweepSumTHD = 0
_sweepSumAmpl = 0
_doSample: bool = False


#
def processSweep(thd,ampl):
    global _skip, _eventSampled, _doSample, _sweepSamples, _sweepSumTHD, _sweepSumAmpl

    try:
        if not _doSample:
            return

        # ready?
        if len(thd_) == len(f0_):
            print("Should not happen, len(thd_) == len(f0_)")
            return

        if _eventSampled is None:
            # The _sampled future should exist.
            # If this is not the case, just
            # create it now
            _eventSampled = asyncio.Event()
        else:
            if _eventSampled.is_set():
                print("_eventSampled.is_set()")
                return

        # Skip the first (few) samples to dismiss
        # any switching artefacts.
        _skip += 1
        if _skip < _numberToSkip:
            return

        _sweepSamples += 1
        _sweepSumTHD += thd
        _sweepSumAmpl += ampl

        if _sweepSamples < active[keyTHDAverage]:
            return

        # Plot the THD
        avgTHD = _sweepSumTHD / _sweepSamples
        thd_.append(avgTHD)
        _sweepSumTHD = 0

#        print(f'THD = {np.round(avgTHD,2)}%')
        
        # Plot the amplitude
        avgAmpl = _sweepSumAmpl / _sweepSamples
        ampl_.append(avgAmpl)
        _sweepSumAmpl = 0

        if active[keyTHDPlotAmplitude]:
            mainWindow.thdWidget.plot(f0_,thd_,ampl_)
        else:
            mainWindow.thdWidget.plot(f0_, thd_)
            
        _skip = 0
        _doSample = False
        _sweepSamples = 0
        _eventSampled.set()
    except:
        traceback.print_exc()


_fixTHD_ = []
_fixS0_ = []
_fixS1_ = []


#
def processFix(_fft, _thd, bins):
    global _fixTHD_, _fixS0_, _fixS1_, _skip

    def runningMean(list, value, n):
        if len(list) == n:
            list.pop(0)
        list.append(value)
        return sum(list) / len(list)

    try:
        _skip += 1
        if _skip < _numberToSkip:
            return

        yf = _fft[1]
        yf_dB = Vrms_to_dBVrms(V_to_Vrms(yf))
        s0 = yf_dB[bins[0]]

        _thd = runningMean(_fixTHD_, _thd, active[keyTHDAverage])
        s0 = runningMean(_fixS0_, s0, active[keyTHDAverage])

        mainWindow.ui.lblTHD.setText(r"THD = %.2f" % (_thd,) + "%")
        mainWindow.ui.lblS0.setText(
            "s<sub>0</sub> = %i dB<sub>V<sub>rms</sub></sub>" % (s0,)
        )

        if len(bins) > 1:
            s1 = yf_dB[bins[1]]
            s1 = runningMean(_fixS1_, s1, active[keyTHDAverage])
            mainWindow.ui.lblS1.setText(
                "s<sub>1</sub> = %i dB<sub>V<sub>rms</sub></sub>" % (s1,)
            )

        mainWindow.ui.lblAverage.setText(f"Average over {int(len(_fixTHD_))} samples")
    except:
        traceback.print_exc()


#
def vertical(v,sds_vdiv,sds_offs):
    '''
    Calculate the optimal Volts / division for the
    current oscilloscope signal. The current oscilloscope
    signal is in v.
    
    If the current signal does not fit set limits,
    set the limits 1.25 times the current signal.
    '''
    vmax = np.amax(v)
    vmin = np.amin(v)
    vdiff = vmax - vmin

    if vdiff / 8 > sds_vdiv:
        optimal_vdiv = 1.25 * vdiff / 8
        next_higher_vdiv = vdiv_lookup[vdiv_lookup>optimal_vdiv][0]
        optimal_offs = -(vmax + vmin) / 2
        return False, next_higher_vdiv, optimal_offs
    else:
        return True, sds_vdiv, sds_offs


#
def setVertical(vdiv,offset):
    ch = active[keySDSChannel]-1
    live_sds.sds.setVDiv(ch,vdiv,'exact')
    live_sds.sds.setOffset(ch,offset)
    return


#
async def processWave(wave):
    try:
        try:
            f0 = active[keyTHDf0]
        except:
            return
        
        # time
        t = wave[1][0]
        
        # voltage
        v = wave[1][1]
        
        # Sanity check
        if t is None or v is None:
            return
        if t.ndim != 1 or v.ndim != 1:
            # Not a 1-dimensional array
            return
        if t.shape[0] == 0 or v.shape[0] == 0:
            # Empty array
            return
        if t.shape[0] != v.shape[0]:
            # Time and voltage arrays not same size
            return
        
        sds_vdiv = wave[1][2]
        sds_offs = wave[1][3]

        # see mainWindow.thdWidget.setFrequencyAxis(f0_)
        _max_f = q.Quantity(f0).real * active[keyTHDHarmonics] * 1.25
        _fft = fft((t, v), max_f=_max_f, output="V")
        _thd, bins = thd(
            _fft,
            q.Quantity(f0).real,
            min_level=dbVrms_to_dBV(active[keyTHDFloor]),
            correct_peaks=False,
            harmonics=active[keyTHDHarmonics],
        )

        # FFT plot
        mainWindow.fftWidget.plot(_fft, bins)

        # oscilloscope plot
        mainWindow.oscWidget.plot(wave)

        # zoomed oscilloscope plot, plot 2 periods
        period = 1 / f0
        t = wave[1][0]
        t1 = t[-1]
        t0 = t[0]
        length = t1 - t0
        periods = length / period
        i_mid = int(t.size / 2)
        i_0 = int(i_mid - t.size / periods)
        i_1 = int(i_mid + t.size / periods) - 1

        slice = (i_0, i_1)
        mainWindow.zoomWidget.plot(wave, slice)

        if active[keySDSAutoVertical]:
            # First check if we have a good view of the waveform
            # If the view is not good, we cannot get a good FFT of it.
            # A good view means that we use the full dynamic range
            # of the oscilloscope.
            right, vdiv, offset = vertical(v,sds_vdiv,sds_offs)
            if not right:
                setVertical(vdiv,offset)
                return
        
        # The verticals are set right. Now we can process the wave.
        if runningSweepMode:
            # Record THD and log it in the THD vs. freq graph
            _ampl_pp = np.amax(v) - np.amin(v)
            _ampl_db_vrms = Vrms_to_dBVrms(V_to_Vrms(_ampl_pp/2))
            processSweep(_thd,_ampl_db_vrms)
        else:
            # pass
            processFix(_fft, _thd, bins)

    except:
        traceback.print_exc()


# To not let the garbage collector dispose of the created tasks.
# see: https://docs.python.org/3/library/asyncio-task.html#creating-tasks
tasks = set()


# Gets the settings from mainWindow.ui
# No validation is done
def getSettings():
    settings = dict()

    ui = mainWindow.ui

    # SDG
    settings[keySDGUse] = qCheckState2Bool(ui.checkUseSDG.checkState())
    settings[keySDGChannel] = ui.cboSDG_ch.currentText()

    if ui.tabSDGModulation.currentIndex() == 0:
        settings[keySDGMode] = SDGMode.CW
    elif ui.tabSDGModulation.currentIndex() == 1:
        settings[keySDGMode] = SDGMode.AM
    elif ui.tabSDGModulation.currentIndex() == 2:
        settings[keySDGMode] = SDGMode.FM

    settings[keySDGCWAmplitude] = ui.edtCW_amplitude.text()
    settings[keySDGAMFrequency] = ui.edtAM_freq.text()
    settings[keySDGAMAmplitude] = ui.edtAM_amplitude.text()
    settings[keySDGAMModulationDepth] = ui.edtAM_modDepth.text()
    settings[keySDGFMFrequency] = ui.edtFM_freq.text()
    settings[keySDGFMAmplitude] = ui.edtFM_amplitude.text()
    settings[keySDGFMFrequencyDeviation] = ui.edtFM_freqDev.text()

    if ui.tabSDGFixedSweep.currentIndex() == 0:
        settings[keySDGFixSweep] = SDGFixSweep.FIX
    else:
        settings[keySDGFixSweep] = SDGFixSweep.SWEEP

    settings[keySDGFixedF0] = ui.edtSDGFixed_f0.text()
    settings[keySDGSweepMinFreq] = ui.edtSDGSweep_minFreq.text()
    settings[keySDGSweepMaxFreq] = ui.edtSDGSweep_maxFreq.text()
    settings[keySDGSweepStep] = ui.edtSDGSweep_step.text()

    # SDS
    settings[keySDSChannel] = ui.cboSDS_ch.currentText()
    settings[keySDSAutoVertical] = qCheckState2Bool(
        ui.checkSDS_autoVertical.checkState()
    )
    settings[keySDSAutoTimebase] = qCheckState2Bool(
        ui.checkSDS_autoHorizontal.checkState()
    )
    settings[keySDSPeriods] = ui.edtSDSPeriods.text()

    # THD
    settings[keyTHDFloor] = ui.edtTHDFloor.text()
    settings[keyTHDHarmonics] = ui.edtTHDHarmonics.text()
    settings[keyTHDAverage] = ui.edtTHDAverage.text()

    settings[keyFFTPlotMinY] = ui.edtFFTPlotMinY.text()
    settings[keyFFTPlotMaxY] = ui.edtFFTPlotMaxY.text()
    settings[keyTHDPlotAmplitude] = qCheckState2Bool(ui.edtTHDAmplitude.checkState())

    return settings


#
def validate(settings):
    """
    Validates the current set of parameters
    set in the main window.

    Settings are translated in place from strings to
    numbers etc.

    Returns (True, None) if the combinations of
    parameters are valid.

    Returns (False,str) if the combination is not valid
    where str is an errormessage.
    """

    def validateChannel(key: str) -> int:
        s = settings[key]
        ch = q.Quantity(s).real
        settings[key] = int(ch)
        return int(ch)

    def validateReal(key: str) -> float:
        v = settings[key]
        r = q.Quantity(v).real
        settings[key] = r
        return r

    def validateInt(key: str) -> int:
        v = settings[key]
        r = q.Quantity(v).real
        settings[key] = int(r)
        return int(r)

    try:
        # Check if the UI settings are in the right format
        ch = validateChannel(keySDGChannel)
        if not ch in {1, 2}:
            return False, "Signal generator channel should be either 1 or 2."

        # CW amplitude
        ampl = validateReal(keySDGCWAmplitude)
        if ampl < 0:
            return False, "CW amplitude cannot be negative."
        if ampl > 20:
            return False, "CW amplitude cannot be larger than 20."

        # AM carrier frequency
        f = validateReal(keySDGAMFrequency)
        if f < 0:
            return False, "AM carrier frequency cannot be negative."
        if f > 30_000_000:
            return False, "AM carrier frequency cannot be larger than 30 MHz."

        # AM amplitude
        ampl = validateReal(keySDGAMAmplitude)
        if ampl < 0:
            return False, "AM carrier amplitude cannot be negative."
        if ampl > 20:
            return False, "AM carrier amplitude cannot be larger than 20."

        # AM modulation depth
        depth = validateReal(keySDGAMModulationDepth)
        if depth < 1:
            return False, "AM modulation depth cannot be smaller than 1%."
        if depth > 120:
            return False, "AM modulation depth canno be larger than 120%."

        # FM carrier frequency
        freqFM = validateReal(keySDGFMFrequency)
        if freqFM < 0:
            return False, "FM carrier frequency cannot be negative."
        if freqFM > 30_000_000:
            return False, "FM carrier frequency cannot be larger than 30 MHz."

        # FM carrier amplitude
        ampl = validateReal(keySDGFMAmplitude)
        if ampl < 0:
            return False, "FM carrier amplitude cannot be negative."
        if ampl > 20:
            return False, "FM carrier amplitude cannot be larger than 20."

        # FM frequency deviation
        deviation = validateReal(keySDGFMFrequencyDeviation)
        if deviation > freqFM:
            return (
                False,
                "FM frequency deviation cannot be larger than the FM carrier frequency.",
            )
        if deviation + freqFM > 30_000_000:
            return (
                False,
                "Sum of FM carrier frequency and FM frequency deviation cannot be larger than 30 MHz.",
            )

        freqFixed = validateReal(keySDGFixedF0)
        if freqFixed < 0:
            return False, "Fixed frequency cannot be negative."
        if settings[keySDGMode] in {SDGMode.AM, SDGMode.FM}:
            if freqFixed > 20_000:
                return False, "On the SDG1032X the  modulation frequency cannot be higher than 20 kHz."
        else:
            if freqFixed > 30_000_000:
                return False, "Fixed frequency cannot be larger than 30 MHz."

        sweepMin = validateReal(keySDGSweepMinFreq)
        if sweepMin < 0:
            return False, "Minimum sweep frequency cannot be negative."
        if sweepMin > 30_000_000:
            return False, "Minimum sweep frequency cannot be larger than 30 MHz."

        sweepMax = validateReal(keySDGSweepMaxFreq)
        if sweepMax <= sweepMin:
            return (
                False,
                "Maximum sweep frequency must be larger than the minimum sweep frequency.",
            )
        if settings[keySDGMode] in {SDGMode.AM, SDGMode.FM}:
            if sweepMax > 20_000:
                return False, "On the SDG1032X the  modulation frequency cannot be higher than 20 kHz."
        else:
            if sweepMax > 30_000_000:
                return False, "Maximum sweep step frequency cannot be larger than 30 MHz."

        #        validateInt(keySDGSweep_steps)
        sweepStep = validateReal(keySDGSweepStep)
        if sweepStep < 0:
            return False, "Frequency sweep step cannot be negative."
        if sweepStep > sweepMax - sweepMin:
            return (
                False,
                f"Frequency sweep step cannot be larger than {q.Quantity(sweepMax-sweepMin,'Hz').render(form='si')}.",
            )

        ch = validateChannel(keySDSChannel)
        if not ch in {1, 2}:
            return False, "Oscilloscope channel should be either 1 or 2."

        periods = validateInt(keySDSPeriods)
        if periods < 5:
            return False, "Number of periods should be larger than 4."

        harmonics = validateInt(keyTHDHarmonics)
        if harmonics < 2:
            return False, "Number of harmonics should be larger than 1."

        validateReal(keyTHDFloor)
        thdPlotMinY = validateReal(keyFFTPlotMinY)
        thdPlotMaxY = validateReal(keyFFTPlotMaxY)
        if thdPlotMaxY <= thdPlotMinY:
            return False, "Maximum THD should be larger than minimum THD."

        thdAverage = validateReal(keyTHDAverage)
        if thdAverage < 1:
            return False, "THD average should be larger than 0."

        # Check if the settings amke sense with
        # regard to each other.
    except Exception as e:
        return False, "FormatError"

    return True, None


#
async def setSDGFrequency(settings, freq):
    """
    Sets the applicable frequency on the SDG,
    depending on CW, AM or FM:

    ch = str(settings[keySDGChannel])
    settings[keySDGMode] == SDGModeCW: "C{ch}:BSWV FRQ,{freq}"
    settings[keySDGMode] == SDGModeAM: "C{ch}:MDWV AM,FRQ,{freq}"
    settings[keySDGMode] == SDGModeFM: "C{ch}:MDWV FM,FRQ,{freq}"
    """
    active[keyTHDf0] = freq
    ch = str(settings[keySDGChannel])
    if settings[keySDGMode] == SDGMode.CW:
        cmd = f"C{ch}:BSWV FRQ,{freq}"
    elif settings[keySDGMode] == SDGMode.AM:
        cmd = f"C{ch}:MDWV AM,FRQ,{freq}"
    elif settings[keySDGMode] == SDGMode.FM:
        cmd = f"C{ch}:MDWV FM,FRQ,{freq}"
    await sdgSend(cmd)


def timebase(f0):
    """
    Returns the most suitable timebase for
    THD calculation with fundamental frequency f0.
    """
    period = 1 / f0
    tb = active[keySDSPeriods] * period / live_sds.sds.divisions()
    return tb


#
def setFFTMaximumFrequency(f0):
    _max = f0 * active[keyTHDHarmonics] * 1.25
    mainWindow.fftWidget.axL.set_xlim(0, _max)
    mainWindow.fftWidget.canvas.draw()


#
async def startFix(settings):
    """
    Starts the fixed mode process.
    This will only set the fixed (modulation) frequency,
    and return immediately. The fix mode process
    is a free running process, only halts on user request.
    """
    global live_sds, _fixTHD_, _fixS0_, _fixS1_, _skip

    active[keyTHDf0] = settings[keySDGFixedF0]

    # Set the FFT maximum frequency
    setFFTMaximumFrequency(active[keyTHDf0])

    # Set oscilloscope timebase
    if settings[keySDSAutoTimebase]:
        tb = timebase(settings[keySDGFixedF0])
        live_sds.sds.setTimebaseAtLeast(tb)

    _fixTHD_ = []
    _fixS0_ = []
    _fixS1_ = []
    _skip = 0


    # Set the SDG
    if settings[keySDGUse]:
        await setSDGFrequency(settings, settings[keySDGFixedF0])


#
async def runSweep(settings):
    """
    Run the sweep mode process. Will stop when the
    sweep has been finished. When the sweep has
    been finished, the _eventRunFinished event
    will be set so other processes can react to that.

    - Loop over the (modulation) frequency range.
    - For every frequency:
      - Set the frequency on the SDG
      - Set the THD f0
    - For every (modulation) frequency, record the
      THD and log it in the THD vs. freq graph.
    """
    global f0_, thd_, ampl_, _eventSampled, _doSample, _sweepSamples, _sweepSumTHD

    fMin = settings[keySDGSweepMinFreq]
    fMax = settings[keySDGSweepMaxFreq]
    step = settings[keySDGSweepStep]

    # Create an array with the frequencies
    # to be tested at. Make np.arange create
    # a closed interval
    _fMax = fMax
    if (_fMax - fMin) % step == 0:
        _fMax += step
    f0_ = np.arange(fMin, _fMax, step)

    # empty the global thd list
    thd_ = []
    ampl_ = []

#    mainWindow.thdWidget.resetTHDAxis()
    mainWindow.thdWidget.setFrequencyAxis(f0_)
    if active[keyTHDPlotAmplitude]:
        mainWindow.thdWidget.rightAxis('Amplitude (dBvrms)')
    else:
        mainWindow.thdWidget.no_rightAxis()

    # Loop over all frequencies in the sweep
    for freq in f0_:
        # Set the current sweep frequency
        active[keyTHDf0] = freq

        # Set the frequency axis in the plot
        setFFTMaximumFrequency(freq)

        # Automatic timebase?
        if settings[keySDSAutoTimebase]:
            tb = timebase(freq)
            #            await live_sds.sds.async_setTimebaseAtLeast(tb)
            live_sds.sds.setTimebaseAtLeast(tb)

        _eventSampled = asyncio.Event()
        await setSDGFrequency(settings, freq)
        _sweepSamples = 0
        _sweepSumTHD = 0
        _doSample = True
        await _eventSampled.wait()
        #        _doSample = False
        _eventSampled = None
        if _cancelSweep:
            break
    _eventRunFinished.set()


#
async def sdgSend(cmd):
    log(cmd)
    # try:
    #     await sdg.async_send(cmd)
    # except Exception as e:
    #     log(f"Fail: {repr(e)}")
    sdg.send(cmd)
    await asyncio.sleep(0)


#
async def sdsSend(cmd):
    log(cmd)
    live_sds.sds.send(cmd)
    await asyncio.sleep(0)


#
async def setupSDGandSDS(settings):
    global sdg, active, live_sds, tasks, runningSweepMode

    if settings[keySDGUse]:
        # SDG
        if sdg is None:
            sdg = SDG(sdgIP, sdgPort, use_visa=sdgUseVisa,query_delay = sdgQueryDelay)

        # Reset
        cmd = "*RST"
        await sdgSend(cmd)

        # Format decimal point
        cmd = "NBFM PNT,DOT"
        await sdgSend(cmd)

        # Format separator
        cmd = "NBFM SEPT,OFF"
        await sdgSend(cmd)

        # switch on SDG channel
        cmd = f"C{settings[keySDGChannel]}:OUTP ON"
        await sdgSend(cmd)

        # Set waveform for the channel to sine
        cmd = f"C{settings[keySDGChannel]}:BSWV WVTP,SINE"
        await sdgSend(cmd)

        # Set frequency, amplitude, modulation
        if settings[keySDGMode] == SDGMode.CW:
            freq = settings[keySDGFixedF0]
            amp = settings[keySDGCWAmplitude]
            mod = None
        elif settings[keySDGMode] == SDGMode.AM:
            freq = settings[keySDGAMFrequency]
            amp = settings[keySDGAMAmplitude]
            mod = "AM"
        if settings[keySDGMode] == SDGMode.FM:
            freq = settings[keySDGFMFrequency]
            amp = settings[keySDGFMAmplitude]
            mod = "FM"

        # set carrier frequency
        cmd = f"C{str(settings[keySDGChannel])}:BSWV FRQ,{freq}"
        await sdgSend(cmd)

        # Set carrier amplitude
        cmd = f"C{settings[keySDGChannel]}:BSWV AMP,{amp}"
        await sdgSend(cmd)

        # Set modulation
        if mod is not None:
            # switch modulation ON
            cmd = f"C{str(settings[keySDGChannel])}:MDWV STATE, ON"
            await sdgSend(cmd)

            # modulation type, AM or FM
            cmd = f"C{str(settings[keySDGChannel])}:MDWV {mod}"
            await sdgSend(cmd)
            #
            if mod == "AM":
                # internal signal source
                cmd = f"C{str(settings[keySDGChannel])}:MDWV AM, SRC, INT"
                await sdgSend(cmd)
                # sine modulation
                cmd = f"C{str(settings[keySDGChannel])}:MDWV AM, MDSP, SINE"
                await sdgSend(cmd)
                # modulation depth
                par = "AM, DEPTH"
                val = settings[keySDGAMModulationDepth]
                cmd = f"C{str(settings[keySDGChannel])}:MDWV {par},{val}"
                await sdgSend(cmd)
            else:
                # FM
                # internal signal source
                cmd = f"C{str(settings[keySDGChannel])}:MDWV FM,SRC,INT"
                await sdgSend(cmd)
                # sine modulation
                cmd = f"C{str(settings[keySDGChannel])}:MDWV FM,MDSP,SINE"
                await sdgSend(cmd)
                # modulation frequency
                if settings[keySDGFixSweep] == SDGFixSweep.FIX:
                    par = "FM,FRQ"
                    val = settings[keySDGFixedF0]
                    cmd = f"C{str(settings[keySDGChannel])}:MDWV {par},{val}"
                    await sdgSend(cmd)
                # modulation deviation
                par = "FM,DEVI"
                val = settings[keySDGFMFrequencyDeviation]
                cmd = f"C{str(settings[keySDGChannel])}:MDWV {par},{val}"
                await sdgSend(cmd)

    # SDS
    
    # Switch on channel
    await sdsSend(f'C{int(active[keySDSChannel])}:TRA ON')

    # AC coupling    
    await sdsSend(f'C{int(active[keySDSChannel])}:CPL A1M')
    
    # Zero Vertical offset
    await sdsSend(f'C{int(active[keySDSChannel])}:OFST 0')
    
    # Trigger
    await sdsSend(f'C{int(active[keySDSChannel])}:TRCP AC')
    await sdsSend(f'TRIG_MODE AUTO')
    await sdsSend(f'TRSE EDGE,SR,C{int(active[keySDSChannel])},HT,OFF')
    await sdsSend('SET50')
    
    # THD

    # Calculate the maximum frequency we need for proper
    # THD calculation
    runningSweepMode = settings[keySDGFixSweep] == SDGFixSweep.SWEEP
    # try:
    #     if runningSweepMode:
    #         # TODO This is not correct.
    #         # In sweep mode, the THDMaxFrequency depends on the current
    #         # frequency (and NOT the max sweep frequency) and the
    #         # number of harmonics.
    #         settings[keyTHDMaxFrequency] = SDGSweepMaximumFrequency() * thdHarmonics()
    #     else:
    #         settings[keyTHDMaxFrequency] = SDGFixedF0() * thdHarmonics()
    #     log(f"Max freq = {q.Quantity(active[keyTHDMaxFrequency],'Hz').render(form='si')}")
    # except:
    #     traceback.print_exc()
    return


#
async def run(settings):
    """
    Performs the THD measurement according to the active paramters.

    The parameters already have been checked and made active.
    """
    global active, live_sds, tasks, runningSweepMode

    active = copy.deepcopy(settings)

    # Create an oscilloscope process if it does not exist yet.
    live_sds = LiveSDS(
        f"THD from channel {active[keySDSChannel]} SDS1202X-E",
        sdsIP,
        sdsPort,
        active[keySDSChannel] - 1,  # 0-based
        processWave,
        use_uvloop=False,  # For Qt we use qasync's QEventLoop
    )

    # Setup the SDG and SDS
    await setupSDGandSDS(settings)

    mainWindow.fftWidget.axL.set_ylim(active[keyFFTPlotMinY], active[keyFFTPlotMaxY])
    #    mainWindow.fftWidget.ax.set_xlim(0, q.Quantity(active[keyTHDMaxFrequency]).real)
    mainWindow.fftWidget.canvas.draw()

    # Start the oscilloscope proces.
    tasks.add(asyncio.create_task(live_sds.async_start(), name="LIVE_SDS"))

    # Start the fix mode process (immediately returns after that)
    # or run the entire sweep process and only return after that
    # has finished.
    if runningSweepMode:
        await runSweep(settings)
        stopSDS()
    else:
        # In FIX mode we only have to set some SDG things.
        # We leave it free-running mode until the user stops
        # it explicitly. In SWEEP mode a program is run which
        # terminates, ie. it does not free-run like in
        # FIX mode.
        await startFix(settings)

    return True


#
def stopSDS():
    global live_sds
    live_sds.stop()
    live_sds = None


#
def start(window):
    """
    Returns (True,Event) if the start was succesfull,
    (False,str) if not (error in parameters, connecting, ...)
    where str is an errormessage.

    The THD is started and keeps running in the background.
    This function merely starts it, and immediately returns.
    """
    global mainWindow, _cancelSweep, tasks, _eventRunFinished
    mainWindow = window

    # Get the settings from the UI
    settings = getSettings()

    # Check if the settings are valid
    valid, err = validate(settings)
    if not valid:
        return False, err
    else:
        # Run with the current UI settings
        _cancelSweep = False
        _eventRunFinished = asyncio.Event()  # create event BEFORE the run starts
        tasks.add(asyncio.create_task(run(settings), name="run"))
        return True, _eventRunFinished


#
def stop(window):
    global mainWindow, _cancelSweep
    mainWindow = window
    if live_sds is not None:
        stopSDS()
    _cancelSweep = True
    if _eventRunFinished is not None:
        _eventRunFinished.set()
    return True, None
