import numpy as np
import matplotlib.pyplot as plt
from typing import List, Callable, Tuple, Optional

# Function Types
EQUATION = 0
MAP = 1

INTEGRATION_METHOD = "Euler"


class System_Function:
    def __init__(self, f: Callable(List[float], List[float]), type: int):
        self.f = f
        self.type = type


class SystemDescriptor:

    functions: List[System_Function] = []

    manifold: Callable(List[float]) = None

    def __init__(self, function_number: int = 1) -> None:
        self.function_number = function_number

    def add_function(self, function, function_type):
        self.functions.append((function, function_type))
        self.function_number += 1


def integrate(system: SystemDescriptor, x0: List[float], params: List[float],
              step: float) -> Tuple[float, Optional[int]]:
    """
    Euler ODE integration
    """
    event: int = None

    label: int = 0 if not system.manifold else system.manifold(x0)
    f = system.functions[label].f

    x0 += f(x0, params) * step
    if system.manifold:
        if label != system.manifold(x0):
            event = system.manifold(x0)

    return (x0, event)


def traiectory(system: SystemDescriptor, x0: List[float], params: List[float],
               n_steps: int, step: float) -> List[float]:
    pass
