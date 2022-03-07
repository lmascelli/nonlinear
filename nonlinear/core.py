import numpy as np
import matplotlib.pyplot as plt
from typing import List, Callable, Tuple, Optional

# Function Types
EQUATION = 0
MAP = 1

INTEGRATION_METHOD = "Euler"


class System_Function:
    def __init__(self, f: Callable[[np.ndarray, List[float]], np.ndarray],
                 type: int):
        self.f = f
        self.type = type


class SystemDescriptor:

    functions: List[System_Function] = []

    manifold: Optional[Callable[[np.ndarray], int]] = None

    def __init__(self, function_number: int = 1) -> None:
        self.function_number = function_number

    def add_function(self,
                     function: Callable[[np.ndarray, List[float]],
                                        np.ndarray],
                     function_type: int) -> None:
        self.functions.append(System_Function(function, function_type))
        self.function_number += 1


def integrate(system: SystemDescriptor, x0: np.ndarray, params: List[float],
              step: float) -> Tuple[np.ndarray, Optional[int]]:
    """
    Euler ODE integration
    """
    event: Optional[int] = None

    label: int = 0 if not system.manifold else system.manifold(x0)
    f = system.functions[label].f

    x0 += f(x0, params) * step
    if system.manifold:
        if label != system.manifold(x0):
            event = system.manifold(x0)

    return (x0, event)


def traiectory(system: SystemDescriptor, x0: np.ndarray, params: List[float],
               n_steps: int, step: float) -> np.ndarray:
    t_ret = np.zeros(shape=(2, n_steps))
    t_ret[0, 0] = x0[0]
    t_ret[1, 0] = x0[1]
    for i in range(0, n_steps):
        x0, event = integrate(system, x0, params, step)
        if event:
            if system.functions[event].type == MAP:
                t_ret[0, i] = system.functions[event].f(x0, params)
                t_ret[0, i] = system.functions[event].f(x0, params)
        else:
            t_ret[0, i] = x0[0]
            t_ret[1, i] = x0[1]
    return t_ret
