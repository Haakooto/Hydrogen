# Hydrogen
Interactive program for calculating and visualising hydrogen wave functions.

Lets you navigate the different states by increasing and decreasing the quantum numbers **n**, **l** and **m** on the fly.

## Working version is out!
Looks quite shit, slow as hell (actually matplotlibs problem), and many features to be added later.

However, **IT WORKS**.

### Still a work in progress

## Usage
Run main.py. Wave function for groundstate appears as black sphere with red in centre. Bright colour means high probability of finding electron here, black is low. Scroll up/down to increase/decrease cut-off value for probability, followed by mouse click to redraw. Click on up and down arrows to change n, l and m.

## TODO:
- make code cleaner/more structured
- Make maximum R-value dependent on nlm to view wavefunction for higher values of n.
- Improve viewing. Currently shows all points inside, is quite messy
- Give user more info, like value of probability cut-off.
- Label axis
- Make title work. Alternatively add text-box where all sort of info can be presented, similar to interface area.
- Understand masked arrays and why Hydrogen.\_\_call__ works
- Further reasearch alternatives to scatter plot. Preferibly a scalar surface plot.