import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvas
from matplotlib.figure import Figure

import asyncio
import traceback


class LiveWidget(FigureCanvas):

    bg = None
    figure = None
    axL = None
    axR = None
    canvas = None

    def __init__(self, parent=None, ylabel=None, xlabel=None, dpi=100):
        global ax, figure, canvas
        super(LiveWidget, self).__init__(Figure())
        self.setParent(parent)
        self.figure = Figure(dpi=dpi)
        self.canvas = FigureCanvas(self.figure)
        self.axL = self.figure.add_subplot(111)
        self.axL.grid()
        self.axL.set_xlabel(xlabel)
        self.axL.set_ylabel(ylabel)
        self._cid = self.canvas.mpl_connect("resize_event", self.onResize)
        

    #
    def rightAxis(self,label):
        self.axR = self.axL.twinx()
        self.axR.set_ylabel(label)
        
    #
    def no_rightAxis(self):
        self.axR = None
        
    #
    def onResize(self, event):
        self.redraw()

    #
    def draw(self, artist, axes=None):
        """
        Draws the artist(s) by way of blitting.
        The artists should have been prepared by

        ax.plot(..., animated=True)

        where ax is the ax attribute of this class.
        
        Parameters:
        axes:   dict{artist,axis} dictates on which axis to draw
                the artist. If None, all artists are drawn on the
                left axis.
        """
        try:
            # Make sure we have an empty background to start with.
            if self.bg is None:
                self.canvas.draw()
                self.bg = self.canvas.copy_from_bbox(self.axL.bbox)

            # Now restore the empty background and redraw the changed artists.
            if artist is not None:
                self.canvas.restore_region(self.bg)
                # convert artist to iterable artists
                try:
                    _ = iter(artist)
                    artists = artist
                except TypeError:
                    artists = [artist]
                for a in artists:
                    if a is not None:
                        if axes is None:
                            axDraw = self.axL
                        else:
                            axDraw = axes[a]
                        axDraw.draw_artist(a)
            self.canvas.blit(self.axL.bbox)
        except:
            traceback.print_exc()

    #
    def redraw(self):
        """
        Force a redraw of the entire figure.
        This may be used in the following
        example cases:

        - one of the axes has changed
          and the ticks need to be redrawn.
        - the title has changed

        Returns: None
        """
        self.bg = None
