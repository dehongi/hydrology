import numpy as np
from scipy.special import expi

def darcy_velocity(K, dh, dl):
    """
    Darcy's Law: v = -K * dh/dl
    """
    return -K * (dh / dl)

def thiem_solution(Q, r1, r2, h1, h2, K=None, T=None):
    """
    Steady state flow to a well in a confined aquifer.
    T = Q * ln(r2/r1) / (2 * pi * (h2 - h1))
    """
    if T is None and K is not None and h2 is not None:
        # Assuming b is implied in h for unconfined or given elsewhere
        pass
    
    T = (Q * np.log(r2 / r1)) / (2 * np.pi * (h2 - h1))
    return T

def theis_solution(T, S, r, t, Q):
    """
    Unsteady flow to a well in a confined aquifer.
    s = (Q / (4 * pi * T)) * W(u)
    u = (r^2 * S) / (4 * T * t)
    W(u) is the well function (exponential integral).
    """
    u = (r**2 * S) / (4 * T * t)
    Wu = -expi(-u)
    s = (Q / (4 * np.pi * T)) * Wu
    return s
