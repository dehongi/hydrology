import numpy as np

def thiessen_polygons(precipitations, weights):
    """
    Calculate areal average precipitation using Thiessen Polygons method.
    
    Args:
        precipitations (list or np.array): Precipitation at each station.
        weights (list or np.array): Weights for each station (usually station area / total area).
        
    Returns:
        float: Areal average precipitation.
    """
    precipitations = np.array(precipitations)
    weights = np.array(weights)
    return np.sum(precipitations * weights) / np.sum(weights)

def arithmetic_mean(precipitations):
    """
    Calculate areal average precipitation using Arithmetic Mean method.
    """
    return np.mean(precipitations)

def isohyetal_method(isohyet_values, area_between_isohyets):
    """
    Calculate areal average precipitation using Isohyetal method.
    
    Args:
        isohyet_values (list): Values of isohyets (n+1 values).
        area_between_isohyets (list): Area between each pair of isohyets (n values).
    """
    isohyet_values = np.array(isohyet_values)
    area_between_isohyets = np.array(area_between_isohyets)
    
    mean_precip = (isohyet_values[:-1] + isohyet_values[1:]) / 2
    return np.sum(mean_precip * area_between_isohyets) / np.sum(area_between_isohyets)

def idf_curve(intensity_params, duration):
    """
    Calculate rainfall intensity using IDF relationship: i = c / (d^e + f)
    Standard Sherman equation.
    """
    c, e, f = intensity_params
    return c / (duration**e + f)
