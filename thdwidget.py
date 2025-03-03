from math import floor

import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvas
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

from pydatacq import SDS, LiveSDS
from fft_calculations import V_to_Vrms, Vrms_to_dBVrms, fft, thd
import quantiphy as q
import numpy as np

from livewidget import LiveWidget


#
class THDWidget(LiveWidget):

    lineTHD = None
    lineAmpl = None

    def __init__(
        self, parent=None, ylabel="THD (%)", xlabel="Fundamental Frequency", dpi=100
    ):
        super().__init__(parent=parent, ylabel=ylabel, xlabel=xlabel, dpi=dpi)
        self.axL.xaxis.set_major_formatter(self.XAxis_Formatter)

    #
    def XAxis_Formatter(self, x, pos):
        return q.Quantity(x, "Hz").render(form="si")

    #
    def resetLines(self):
        self.lineAmpl = None
        self.lineTHD = None
                
    #
    def newPlot(self, f0_):
        self.f0_ = f0_
        self.axL.set_xlim(f0_[0], f0_[-1])
        for ax in self.figure.axes:
            for art in ax.lines:
                art.remove()
        if self.axR in self.figure.axes:
            self.figure.delaxes(self.axR)
        self.resetLines()
        self.canvas.draw()

    #
    def plot(self, f0_, thd_, ampl_=None):

        def logLimits(ampl_):
            """
            Returns low and high limits to use
            for the logarithmic amplitude scale.

            Returns the smallest multiple of 10dB
            in which the entire ampl_ range fits.
            """
            k = 10
            low = np.amin(ampl_)
            low = int(low // k) * k
            high = np.amax(ampl_)
            high = (int(high // k) + 1) * k
            return low, high

        def limit125(max: float)-> int:
            '''
            Returns the limit for the y-axis in a 1-2-5 regime.
            '''
            log = floor(np.log10(max))
            # max in [.01 .. .1>: log = -2
            # max in [.1 .. 1>: log = -1
            # max in [1 .. 10>: log = 0
            # max in [10 .. 100>: log = 1
            # max in [100 .. 1000>: log = 2
            first_digit = int(max / (10 ** log))
            if first_digit < 1:
                range = 1
            elif first_digit < 2:
                range = 2
            elif first_digit < 5:
                range = 5
            else:
                range = 10
            return range * 10 ** log
        
        x_ = f0_[0 : len(thd_)]

        # Plot THD
        y_ = np.array(thd_)
        max = np.amax(y_)
        self.axL.set_ylim(0,limit125(max))
        if self.lineTHD is None:
            (self.lineTHD,) = self.axL.plot(x_, y_, "green", linewidth=2)
        else:
            self.lineTHD.set_data(x_, y_)

        if ampl_ is not None and self.axR is not None:
            # Plot amplitude
            y_ = np.array(ampl_)
            if self.lineAmpl is None:
                (self.lineAmpl,) = self.axR.plot(x_, y_, "green", ls="--", linewidth=2)
            else:
                self.lineAmpl.set_data(x_, y_)
            self.axR.set_ylim(logLimits(ampl_))

        self.canvas.draw()


#