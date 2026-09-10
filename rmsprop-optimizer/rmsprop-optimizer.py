import numpy as np

def rmsprop_step(
    w: list,
    g: list,
    s: list,
    lr: float = 0.001,
    beta: float = 0.9,
    eps: float = 1e-8,
) -> tuple[list, list]:
    """
    Returns (new_w, new_s) with the same shapes as the inputs.
    """
    # Write code here
    w_first = np.array(w, dtype = np.float64)
    g_first = np.array(g, dtype = np.float64)
    s_first = np.array(s, dtype = np.float64)

    #Step 1
    new_s = beta * s_first + (1 - beta) * (g_first ** 2)
    new_w = w_first - (lr / (np.sqrt(new_s + eps)) * g_first)    

    return new_w, new_s
    
    
    pass