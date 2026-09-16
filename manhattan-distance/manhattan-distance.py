import numpy as np

def manhattan_distance(x: list, y: list) -> float:
    """
    Returns the Manhattan distance as a Python float.
    """
    # Write code here
    xi = np.array(x, dtype = np.float64)
    yi = np.array(y, dtype = np.float64)

    distance = np.sum(np.abs(xi - yi))
    return distance
    pass