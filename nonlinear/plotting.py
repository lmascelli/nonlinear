import matplotlib.pyplot as plt
import numpy as np
from typing import List, Optional


def vector_field(vf: List[List[np.ndarray]], xrange: List[float],
                 yrange: List[float], points: List[int],
                 axes: Optional[plt.Axes]) -> None:
    x = np.linspace(xrange[0], xrange[1], points[0])
    y = np.linspace(yrange[0], yrange[1], points[1])

    for i in range(0, points[0]):
        for j in range(0, points[1]):
            if axes:
                axes.quiver(x[i], y[j], vf[j][i][0], vf[j][i][1],
                            width=0.003,
                            scale=1000)
            else:
                plt.quiver(x[i], y[j], vf[j][i][0], vf[j][i][1],
                           width=0.001,
                           scale=1000)
