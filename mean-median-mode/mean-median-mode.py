from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    # Write code here
    xi = np.array(x, dtype = np.float64)

    mean_val = float(np.mean(xi))
    median_val = float(np.median(xi))

    counts = Counter(x)
    max_counts = max(counts.values())

    modes = [k for k, v in counts.items() if v == max_counts]
    mode_val = float(min(modes))

    return {"mean" : mean_val, "median" : median_val, "mode" : mode_val}
    pass