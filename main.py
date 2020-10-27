import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
from nlmInterface import Interface, Hydrogen


def tellme(s):
    plt.title(s)
    draw()

def draw():
    x, y, z, c = Hydrogen()
    Plot._offsets3d = (x, y, z)
    fig.colorbar(Plot)
    plt.draw()

def mouse_click(event):
    Interface.contains(event)
    tellme(f"n = {Hydrogen.n}, l = {Hydrogen.l}, m = {Hydrogen.m}")

# def draw(Plot):
#     Plot[0].set_ydata(y())


fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
cid = fig.canvas.mpl_connect("button_press_event", mouse_click)

ax.add_artist(Interface)

x, y, z, c = Hydrogen()
Plot = ax.scatter(x, y, z, c=c, cmap=plt.hot())

# this = Plot._offsets3d
# print(this)
# print(dir(Plot))

# draw(Plot)

plt.show()
