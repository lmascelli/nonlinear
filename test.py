import matplotlib.pyplot as plt
import numpy as np

from nonlinear import core, plotting
from typing import List


######################################################
#
#               The system equations
#
######################################################


def f(x: np.ndarray, params: List[float]) -> np.ndarray:
    a = 0.04
    b = 5.
    c = 150.
    return np.array([
        a * np.power(x[0], 2) + b * x[0] + c - x[1],
        params[0]*(params[1]*x[0]-x[1])
    ])


def map_f(x: np.ndarray, _: List[float]) -> np.ndarray:
    d = -55
    f = 4
    return np.array([d, x[1] + f])


def manifold(x: np.ndarray) -> int:
    return 1 if x[0] > 30 else 0


################# System Descriptor ##################
system = core.SystemDescriptor()
system.add_function(f, core.EQUATION)
system.add_function(map_f, core.MAP)
system.manifold = manifold


######################################################
#
#                   Analysis script
#
######################################################


### Vector field of the system varying a parameter ###

params = [0.1, 1]
xrange = [-100., 35.]
yrange = [-100., 100.]
sampling_points = [30, 30]

vf = core.vector_field(system, params, xrange, yrange, sampling_points)


def on_key_press(event):
    global vf, ax, fig
    if event.key == 'd' and params[0] < 1:
        print('Increasing alpha')
        params[0] += 0.1
    if event.key == 'a' and params[0] > 0:
        print('Decreasing alpha')
        params[0] -= 0.1
    if event.key == 'w' and params[1] < 1:
        print('Increasing betha')
        params[1] += 0.1
    if event.key == 'r' and params[1] > 0:
        print('Decreasing betha')
        params[1] -= 0.1
    vf = core.vector_field(system, params, xrange, yrange, sampling_points)
    ax.clear()
    plotting.vector_field(vf, xrange, yrange, sampling_points, ax)
    fig.canvas.draw()


fig, ax = plt.subplots()
fig.canvas.mpl_connect('key_press_event', on_key_press)
plotting.vector_field(vf, xrange, yrange, sampling_points, ax)
plt.show()
