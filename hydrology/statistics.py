import numpy as np
from scipy import stats

def gumbel_distribution_params(data):
    """
    Estimate Gumbel (EVI) parameters using moments.
    """
    mean = np.mean(data)
    std = np.std(data)
    alpha = np.sqrt(6) * std / np.pi
    u = mean - 0.5772 * alpha
    return u, alpha

def gumbel_value(return_period, u, alpha):
    """
    Calculate value for a given return period T.
    y = -ln(-ln(1 - 1/T))
    x = u + alpha * y
    """
    y = -np.log(-np.log(1 - 1/return_period))
    return u + alpha * y

def log_pearson_type_3_params(data):
    """
    Estimate LP3 parameters.
    """
    log_data = np.log10(data)
    mean = np.mean(log_data)
    std = np.std(log_data)
    skew = stats.skew(log_data)
    return mean, std, skew

def log_pearson_type_3_value(return_period, mean, std, skew):
    """
    Calculate LP3 value for a given return period.
    Needs frequency factor K from tables or approximation.
    """
    # Placeholder for K approximation
    pass
