import numpy as np
from hydrology.precipitation import thiessen_polygons
from hydrology.infiltration import horton_infiltration
from hydrology.runoff import rational_method, unit_hydrograph_convolution
from hydrology.routing import muskingum_routing

def main():
    print("--- Hydrology Library Demo ---")
    
    # Precipitation
    p_stations = [12.5, 15.2, 10.8, 14.1]
    weights = [0.1, 0.4, 0.3, 0.2]
    areal_p = thiessen_polygons(p_stations, weights)
    print(f"Areal Precipitation (Thiessen): {areal_p:.2f} mm")
    
    # Infiltration
    t = np.linspace(0, 5, 6)
    f = horton_infiltration(f0=12, fc=3, k=0.8, t=t)
    print(f"Horton Infiltration rates over 5 hours: {f}")
    
    # Runoff
    excess_rainfall = [1.0, 2.0, 1.5]
    uh = [0.1, 0.5, 0.3, 0.1]
    direct_runoff = unit_hydrograph_convolution(excess_rainfall, uh)
    print(f"Direct Runoff Hydrograph: {direct_runoff}")
    
    # Routing
    inflow = np.array([10, 20, 50, 40, 30, 20, 15, 10])
    outflow = muskingum_routing(inflow, K=2.0, X=0.2, delta_t=1.0, O1=10)
    print(f"Muskingum Outflow: {outflow}")

if __name__ == "__main__":
    main()
