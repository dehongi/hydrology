import pytest
import numpy as np
from hydrology.precipitation import thiessen_polygons, arithmetic_mean, isohyetal_method
from hydrology.infiltration import horton_infiltration, scs_curve_number_runoff
from hydrology.runoff import rational_method

def test_precipitation():
    p = [10, 20, 30]
    w = [0.2, 0.5, 0.3]
    assert thiessen_polygons(p, w) == (10*0.2 + 20*0.5 + 30*0.3)
    assert arithmetic_mean(p) == 20

def test_isohyetal():
    isohyets = [10, 20, 30]
    areas = [100, 200]
    # Mean precip: (10+20)/2 = 15, (20+30)/2 = 25
    # Areal average: (15*100 + 25*200) / 300 = (1500 + 5000) / 300 = 6500 / 300 = 21.666...
    assert isohyetal_method(isohyets, areas) == pytest.approx(21.66666667)

def test_horton():
    f = horton_infiltration(f0=10, fc=2, k=0.5, t=1)
    # f = 2 + (10 - 2) * e^(-0.5*1) = 2 + 8 * 0.6065 = 2 + 4.852 = 6.852
    assert f == pytest.approx(6.852, rel=1e-3)

def test_scs_runoff():
    # P = 5, CN = 80 => S = 1000/80 - 10 = 12.5 - 10 = 2.5
    # Ia = 0.2 * 2.5 = 0.5
    # Pe = (5 - 0.5)^2 / (5 - 0.5 + 2.5) = 4.5^2 / 7 = 20.25 / 7 = 2.8928
    assert scs_curve_number_runoff(5, 80) == pytest.approx(2.8928, rel=1e-3)
    assert scs_curve_number_runoff(0.1, 80) == 0.0

def test_rational():
    assert rational_method(0.6, 2.0, 100) == 120.0
