import numpy as np

def thornthwaite_et(T_monthly, annual_heat_index=None):
    """
    Calculate potential evapotranspiration (PET) using Thornthwaite's method.
    ET = 16 * (10*T / I)^a
    
    Args:
        T_monthly: Mean monthly temperature (Celsius)
        annual_heat_index (I): Sum of (Ti/5)^1.514
    """
    T = np.array(T_monthly)
    if annual_heat_index is None:
        # Assuming T_monthly is a full year if I is not provided
        I = np.sum((np.maximum(T, 0) / 5)**1.514)
    else:
        I = annual_heat_index
        
    a = (6.75e-7 * I**3) - (7.71e-5 * I**2) + (1.792e-2 * I) + 0.49239
    
    pet = 16 * (10 * T / I)**a
    return pet

def priestley_taylor(Rn, G, T_celsius, alpha=1.26):
    """
    Priestley-Taylor equation for PET.
    ET = alpha * (delta / (delta + gamma)) * (Rn - G) / lambda
    
    Args:
        Rn: Net radiation (MJ/m2/day)
        G: Soil heat flux (MJ/m2/day)
        T_celsius: Temperature (C)
        alpha: Empirical coefficient (default 1.26)
    """
    # Slope of saturation vapor pressure curve
    delta = 4098 * (0.6108 * np.exp(17.27 * T_celsius / (T_celsius + 237.3))) / (T_celsius + 237.3)**2
    # Psychrometric constant (approx 0.067 kPa/C at sea level)
    gamma = 0.067 
    # Latent heat of vaporization (approx 2.45 MJ/kg)
    lmbda = 2.45
    
    pet = alpha * (delta / (delta + gamma)) * (Rn - G) / lmbda
    return pet

def penman_monteith(Rn, G, T, u2, es, ea, delta, gamma):
    """
    FAO-56 Penman-Monteith equation for reference ET.
    Simplified version usually used in hydrology.
    """
    numerator = 0.408 * delta * (Rn - G) + gamma * (900 / (T + 273)) * u2 * (es - ea)
    denominator = delta + gamma * (1 + 0.34 * u2)
    return numerator / denominator
