import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
from nlmInterface import Interface, Hydrogen  # * Instances, not classes


def tellme(s):
    """ Sets title and redraws """
    plt.title(s)
    draw()

def draw():
    """ Should be called to redraw figure """
    # x, y, z, c = Hydrogen()
    # Plot._offsets3d = (x, y, z)
    # fig.colorbar(Plot)
    plt.draw()

def mouse_click(event):
    """ Handles mouse click events """
    Interface.contains(event)
    tellme(f"n = {Hydrogen.n}, l = {Hydrogen.l}, m = {Hydrogen.m}")

def key_click(event):
    if event.key == "b":
        print(ax.azim)

# def draw(Plot):
#     Plot[0].set_ydata(y())


fig = plt.figure()
ax = fig.add_subplot(111, projection="3d") # ! 3D for production
# ax = fig.add_subplot(111) # ! 2D for testing
cid = fig.canvas.mpl_connect("button_press_event", mouse_click)
cid = fig.canvas.mpl_connect("key_press_event", key_click)

ax.add_artist(Interface)

x, y, z, c = Hydrogen()
Plot = ax.scatter(x, y, z, c=c, cmap=plt.hot())

# this = Plot._offsets3d
# print(this)
# print(dir(Plot))

# draw(Plot)

plt.show()
