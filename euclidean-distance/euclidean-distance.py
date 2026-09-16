import numpy as np

def euclidean_distance(x: list, y: list) -> float:
    """
    Returns the Euclidean distance as a Python float.
    """
    # Write code here
    xi = np.array(x, dtype = np.float64)
    yi = np.array(y, dtype = np.float64)
    distance = np.sqrt(np.sum((xi-yi)**2))
    return distance 
    pass