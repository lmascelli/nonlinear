import matplotlib.pyplot as plt
import numpy as np
from typing import List

def vector_field(vf: List[List[np.ndarray]], xrange: List[float],
        yrange: List[float], points: List[int]) -> None:
    x = np.linspace(xrange[0], xrange[1], points[0])
    y = np.linspace(yrange[0], yrange[1], points[1])

    for i in range(0, points[0]):
        for j in range(0, points[1]):
            plt.quiver([x[i], y[j]], vf[j][i])
