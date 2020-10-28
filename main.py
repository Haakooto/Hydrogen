import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
from Interface import Interface, Hydrogen  # * Instances, not classes


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

    x, y, z, c = Hydrogen()
    ax.scatter(x, y, z, c=c, cmap=plt.hot())
    ax.set_xlim(np.min(z), np.max(z))
    ax.set_ylim(np.min(z), np.max(z))

    plt.draw()

def mouse_click(event):
    """ Handles mouse click events """
    Interface.contains(event)
    tellme(f"n = {Hydrogen.n}, l = {Hydrogen.l}, m = {Hydrogen.m}")
    draw()


def key_click(event):
    if event.key == "b":
        print(ax.azim)
        print(ax.elev)
        print(ax.dist)
    if event.key == "d":
        tellme(Hydrogen.prob)
        draw()
    if event.key == "n":
        Interface.area._children[-1].set_text(Hydrogen.m)
        draw()

def scroll(event):
    if event.button == "up":
        Hydrogen.up()
    elif event.button == "down":
        Hydrogen.down()


fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
cid = fig.canvas.mpl_connect("button_press_event", mouse_click)
cid = fig.canvas.mpl_connect("key_press_event", key_click)
cid = fig.canvas.mpl_connect("scroll_event", scroll)

draw()
tellme("testtest")

plt.show()
