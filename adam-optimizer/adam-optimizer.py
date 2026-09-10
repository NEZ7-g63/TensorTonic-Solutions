import numpy as np

def adam_step(
    param: list,
    grad: list,
    m: list,
    v: list,
    t: int,
    lr: float = 1e-3,
    beta1: float = 0.9,
    beta2: float = 0.999,
    eps: float = 1e-8,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Returns (param_new, m_new, v_new) as NumPy arrays.
    """
    # Write code here
    p = np.array(param, dtype = np.float64)
    g = np.array(grad, dtype = np.float64)
    firstM = np.array(m, np.float64)        
    secondV = np.array(v, np.float64)

    # First and Second Moment
    first_M = beta1 * firstM + (1 - beta1)*g
    second_V = beta2 * secondV + (1 - beta2)* np.square(g)

    # Bias Correction
    m_new = first_M / (1-(beta1**t))
    v_new = second_V / (1 - (beta2**t))

    # Parameter Update
    param_new = p - lr*(m_new/(np.sqrt(v_new)+eps))

    return param_new, first_M, second_V
    pass