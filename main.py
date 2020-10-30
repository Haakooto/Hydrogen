import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
from Interface import Interface, Hydrogen  # * Instances, not classes
# from myplotlib import Axes3D


def tellme(s):
    """ Sets title"""
    ax.set_title(s)

def draw():
    """ Should be called to redraw figure """
    ax.cla()

    Interface.set_text(-3, Hydrogen.n)
    Interface.set_text(-2, Hydrogen.l)
    Interface.set_text(-1, Hydrogen.m)
    ax.add_artist(Interface)

    for rand in ((1, 0.6), (0.1, 0.01), (0.001, 0.0001)):
        x, y, z, c = Hydrogen(*rand)
    # a = int(np.sqrt(c.shape[0]))
    # c = c.reshape((a, a))
    # x = x.reshape((a, a))
    # y = y.reshape((a, a))
        ax.scatter(x, y, z, c=c, cmap=plt.hot())
    # ax.contour(x, y, c, cmap=plt.hot())
    # ax.plot(x)
    # ax.set_xlim(np.min(z), np.max(z))
    # ax.set_ylim(np.min(z), np.max(z))

    plt.draw()
    return

def mouse_click(event):
    """ Handles mouse click events """
    if Interface.contains(event):
        draw()
    tellme(f"n = {Hydrogen.n}, l = {Hydrogen.l}, m = {Hydrogen.m}")


def key_click(event):
    pass
#     if event.key == "b":
#         print(ax.azim)
#         print(ax.elev)
#         print(ax.dist)
    if event.key == "d":
        tellme(Hydrogen.prob)
        draw()
#     if event.key == "n":
#         Interface.area._children[-1].set_text(Hydrogen.m)
#         draw()

def scroll(event):
    if event.button == "up":
        Hydrogen.up()
    elif event.button == "down":
        Hydrogen.down()


fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
# ax = fig.add_subplot(111)
fig.canvas.mpl_connect("button_press_event", mouse_click)
fig.canvas.mpl_connect("key_press_event", key_click)
fig.canvas.mpl_connect("scroll_event", scroll)


draw()
# fig.colorbar(W)

plt.show()
