import traceback

from matplotlib.backends.backend_qtagg import FigureCanvas
import quantiphy as q
import numpy as np

from livewidget import LiveWidget


class OscWidget(LiveWidget):
    
    line = None
    tmax = None

    _limits = np.array(
        sorted(
            [
                (s * d * 10 ** int(e))
                for d in [1,2,4,5,6,8]
                for e in np.arange(-6, 2)
                for s in [-1, 1]
            ]
        )
    ) 

    #
    def __init__(self, parent=None, ylabel='s (V)', xlabel='time', dpi=100):
        super().__init__(parent,ylabel=ylabel,xlabel=xlabel,dpi=dpi)       
        self.axL.xaxis.set_major_formatter(self.XAxis_Formatter)

    #
    def XAxis_Formatter(self, x, pos):
        return q.Quantity(x, "s").render(form="si")

    #
    def plot(self,wave,slice=None):
        try:
            t = wave[1][0]
            t = t - (t[-1]-t[0])/2
            v = wave[1][1]
            if slice is None:
                pass
            else:
                # size = len(wave[1][0])
                # mid = size / 2
                # i0 = int(mid - size / 2 / self.zoom)
                # i1 = int(mid + size / 2 / self.zoom) - 1
                t = t[slice[0]:slice[1]]
                v = v[slice[0]:slice[1]]

            if self.line is None:
                self.line = self.axL.plot(t,v,animated=True)[0]
            else:
                # We set x and y data here because len(wave) may have changed.
                self.line.set_data(t,v)

            # x-axis ticks logic
            if self.tmax != t[-1]:
                # timebase has changed, redraw everything
                self.axL.set_xlim(t[0],t[-1])
                self.axL.xaxis.set_major_formatter(self.XAxis_Formatter)
                self.redraw()
            self.tmax = t[-1]

            self.draw([self.line])

            v_max = np.amax(v)
            v_min = np.amin(v)
            y_min = self._limits[self._limits < v_min * 1.1][-1]
            y_max = self._limits[self._limits > v_max * 1.1][0]
            _bot, _top = self.axL.get_ylim()
            if _bot != y_min or _top != y_max:
                self.axL.set_ylim(y_min, y_max)
                self.redraw()

        except:
            traceback.print_exc()
        return



