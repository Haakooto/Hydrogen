import matplotlib as mpl
from matplotlib.offsetbox import AnchoredOffsetbox, DrawingArea
from matplotlib.patches import RegularPolygon as RegPoly
from Hydrogen import Hydrogen
from numpy import pi


class AnchoredInterface(AnchoredOffsetbox):
    """
    Fixed object holding drawing area.
    (Box in upper left corner)
    """
    def __init__(self, width, height, xdescent, ydescent):
        self.area = DrawingArea(width, height, xdescent, ydescent)
        super().__init__(loc="upper right", pad=0.4, borderpad=0.5,
                         child=self.area, prop=None, frameon=True)

    def contains(self, mouseevent):
        """
        Check is mouse click is inside
        Returns:
            a: bool
            b: dict
                Is empty dict, can be changed for more info if needed
        """
        for c in self.area.get_children():
            a, b = c.contains(mouseevent)
            if a:
                if callable(c):
                    c()
                return a, b
        return False, {}

    def copy(self):
        A = self.area
        new = AnchoredInterface(A.width, A.height, A.xdescent, A.ydescent)
        for child in A._children:
            new.area.add_artist(child)
        return new


    def set_text(self, childno, text):
        self.area._children[childno].set_text(text)


class ClickableArtist(RegPoly):
    """
    Clickable regular polygon
    Action is function called upon when clicked.
    """
    def __init__(self, action, *args, **kwargs):
        self.action = action
        super().__init__(*args, **kwargs)

    def __call__(self):
        return self.action()


Hydrogen = Hydrogen()
Interface = AnchoredInterface(70, 60, 0, 0)


# TODO Clean up. This looks like shit
# Up and down buttons
nUp = ClickableArtist(Hydrogen.n_inc, (12, 45), 3, 10, orientation=0)
lUp = ClickableArtist(Hydrogen.l_inc, (35, 45), 3, 10, orientation=0)
mUp = ClickableArtist(Hydrogen.m_inc, (58, 45), 3, 10, orientation=0)
nDown = ClickableArtist(Hydrogen.n_dec, (12, 15), 3, 10, orientation=pi)
lDown = ClickableArtist(Hydrogen.l_dec, (35, 15), 3, 10, orientation=pi)
mDown = ClickableArtist(Hydrogen.m_dec, (58, 15), 3, 10, orientation=pi)
# Box for holding "n", "l", "m"
nBox = ClickableArtist(Hydrogen.get_n, (12, 30), 4, 10, orientation=pi/4, fill=False)
lBox = ClickableArtist(Hydrogen.get_l, (35, 30), 4, 10, orientation=pi/4, fill=False)
mBox = ClickableArtist(Hydrogen.get_m, (58, 30), 4, 10, orientation=pi/4, fill=False)
# n, l, m
n = mpl.text.Annotation("n", (0.17, 0.44), xycoords=Interface)
l = mpl.text.Annotation("l", (0.48, 0.43), xycoords=Interface)
m = mpl.text.Annotation("m", (0.74, 0.44), xycoords=Interface)
# add all objects above to Interface
Interface.area.add_artist(nUp)
Interface.area.add_artist(lUp)
Interface.area.add_artist(mUp)
Interface.area.add_artist(nDown)
Interface.area.add_artist(lDown)
Interface.area.add_artist(mDown)
Interface.area.add_artist(nBox)
Interface.area.add_artist(lBox)
Interface.area.add_artist(mBox)
Interface.area.add_artist(n)
Interface.area.add_artist(l)
Interface.area.add_artist(m)
