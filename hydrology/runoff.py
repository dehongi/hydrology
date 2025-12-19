import numpy as np

def rational_method(C, i, A):
    """
    Rational Method for peak discharge: Q = CiA
    
    Args:
        C (float): Runoff coefficient.
        i (float): Rainfall intensity (L/T).
        A (float): Drainage area (L^2).
    """
    return C * i * A

def unit_hydrograph_convolution(excess_rainfall, unit_hydrograph):
    """
    Calculate direct runoff hydrograph by convolving excess rainfall with a unit hydrograph.
    
    Args:
        excess_rainfall (np.array): Sequence of excess rainfall depths.
        unit_hydrograph (np.array): Ordinate of the unit hydrograph.
    """
    return np.convolve(excess_rainfall, unit_hydrograph)[:len(excess_rainfall) + len(unit_hydrograph) - 1]

def scs_unit_hydrograph_peak(A, Tp):
    """
    SCS triangular unit hydrograph peak discharge.
    qp = 484 * A / Tp (English units: cfs, sq.mi, hr)
    qp = 2.08 * A / Tp (SI units: m3/s/cm, km2, hr)
    """
    return 2.08 * A / Tp
