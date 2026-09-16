import numpy as np

def minmax_scale(X: list, axis: int = 0, eps: float = 1e-12) -> np.ndarray:
    """
    Returns a floating-point NumPy array matching the shape of X.
    """
    # Write code here
    X_arr = np.array(X, dtype = np.float64)

    min_val = np.min(X_arr, axis=axis, keepdims=True)
    max_val = np.max(X_arr, axis=axis, keepdims=True)

    range = max_val - min_val
    range = np.where(range == 0, eps, range)
    return (X_arr - min_val)/range
    pass