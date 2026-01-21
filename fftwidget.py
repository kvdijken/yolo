from fft_calculations import V_to_Vrms, Vrms_to_dBVrms
import quantiphy as q

import traceback
import functools

from livewidget import LiveWidget


#
class FFTWidget(LiveWidget):
    bg = None
    figure = None
    ax = None
    canvas = None

    def __init__(
        self, parent=None, ylabel="s (dBVrms)", xlabel="Frequency", dpi=100, hold=False
    ):
        super().__init__(parent, ylabel=ylabel, xlabel=xlabel, dpi=dpi)
        self.axL.xaxis.set_major_formatter(self.XAxis_Formatter)
        
        # on a change in x-ticks redraw everything, mainly because of the grid
        self.axL.callbacks.connect("xlim_changed",functools.partial(self.xlim_changed,self))

    #
    def force_redraw(self):
        self.bg = None
        self.canvas.draw()

    #
    def xlim_changed(self,*a,**kw):
 
        def cla(ax):
            if ax is None:
                return
            for line in ax.get_lines():
                line.remove()
            for coll in ax.collections:
                coll.remove()
 
#        cla(self.axL)
#        cla(self.axR)
        self.force_redraw()
        
    #
    def onResize(self, event):
        self.force_redraw()

    #
    def XAxis_Formatter(self, x, pos):
        return q.Quantity(x, "Hz").render(form="si")

    #
    def plot(self, fft, bins=None):
        '''
        Parameters:

        bins: list of indices in fft[0] and fft[1] where to plot markers.
              If bins is None, then do not plot markers.
        '''
        try:
            items = []

            xf = fft[0]
            yf = fft[1]  # yf in V

            # transform to dBvrms for the display
            yf_dB = Vrms_to_dBVrms(V_to_Vrms(yf))

            if bins is not None:
                # plot a x at harmonics
                for p in bins[1:]:
                    item = self.axL.scatter(
                        xf[p], yf_dB[p], marker=7, color="blue", animated=True
                    )
                    items.append(item)

                # plot a dot at fundamental frequency
                item = self.axL.scatter(
                    xf[bins[0]], yf_dB[bins[0]], marker=7, color="red", animated=True
                )
                items.append(item)

            # plot fft
            item = self.axL.plot(xf, yf_dB, animated=True)[0]
            items.append(item)

            self.draw(items)
        except:
            traceback.print_exc()
