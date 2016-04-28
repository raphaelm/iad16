from tsplib import _latlon
import numpy as np


def test_calc_latlon():
    pi = 3.141592
    a = np.array([[180, 360], [180, 90]])
    assert (_latlon(a) == np.array([[pi, 2*pi], [pi, pi/2]])).all()
