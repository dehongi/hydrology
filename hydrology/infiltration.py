import numpy as np

def horton_infiltration(f0, fc, k, t):
    """
    Calculate infiltration rate using Horton's equation: f(t) = fc + (f0 - fc) * e^(-kt)
    
    Args:
        f0: Initial infiltration capacity (L/T)
        fc: Final equilibrium infiltration capacity (L/T)
        k: Decay constant (1/T)
        t: Time since start (T)
    """
    return fc + (f0 - fc) * np.exp(-k * t)

def horton_cumulative_infiltration(f0, fc, k, t):
    """
    Analytical integral of Horton's equation for cumulative infiltration F(t).
    F(t) = fc*t + (f0 - fc)/k * (1 - e^(-kt))
    """
    return fc * t + ((f0 - fc) / k) * (1 - np.exp(-k * t))

def scs_curve_number_runoff(P, CN, initial_abstraction_ratio=0.2):
    """
    Calculate runoff depth using SCS Curve Number method.
    S = 1000/CN - 10 (inches)
    Ia = 0.2 * S (standard)
    Pe = (P - Ia)^2 / (P - Ia + S)
    """
    S = (1000 / CN) - 10
    Ia = initial_abstraction_ratio * S
    
    if P <= Ia:
        return 0.0
    
    runoff = (P - Ia)**2 / (P - Ia + S)
    return runoff

def green_ampt_infiltration_rate(K, psi, theta_diff, F):
    """
    Green-Ampt infiltration rate: f = K * (1 + (psi * theta_diff / F))
    """
    if F == 0:
        return np.inf
    return K * (1 + (psi * theta_diff / F))
