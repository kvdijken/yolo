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
    def setFrequencyAxis(self, f0_):
        self.f0_ = f0_
        self.axL.set_xlim(f0_[0], f0_[-1])
        for ax in self.figure.axes:
            for art in ax.lines:
                art.remove()
        if self.axR in self.figure.axes:
            self.figure.delaxes(self.axR)
        self.resetLines()

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

        x_ = f0_[0 : len(thd_)]

        # Plot THD
        y_ = np.array(thd_)
        if self.lineTHD is None:
            (self.lineTHD,) = self.axL.plot(x_, y_, "green", linewidth=2)
        else:
            self.lineTHD.set_data(x_, y_)
            max = np.amax(y_)
            k = 0.2
            self.axL.set_ylim(0,(max//k + 1) * k)

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