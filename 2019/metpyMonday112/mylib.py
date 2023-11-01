# Metpy Monday
# 112 - What is 1 - 0.5? Testing Calculations!
# https://www.youtube.com/watch?v=_8Cke2YGDx4

import numpy as np

def wind_speed(u, v):
	""" Computer the wind speed from u and v components. """
	return np.sqrt(u * u + v * v)
