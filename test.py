import matplotlib.pyplot as plt
import numpy as np

from nonlinear import core
from typing import List


def f(x: np.ndarray, params: List[float]) -> np.ndarray:
    a = 0.04
    b = 5
    c = 150
    return np.array([
        a * x[0] * x[0] + b * x[0] + c - x[1],
        params[0]*(params[1]*x[0]-x[1])
    ])


def map_f(x: np.ndarray, _: List[float]) -> np.ndarray:
    d = -55
    f = 4
    return np.array([d, x[1] + f])


system = core.SystemDescriptor()
system.add_function(f, core.EQUATION)
system.add_function(map_f, core.MAP)

x0 = np.array([1., 1.])
params = [0.1, 0.2]

t = core.traiectory(system, x0, params, 500000, 1e-6)
plt.plot(t[0, :], t[1, :])
plt.show()
