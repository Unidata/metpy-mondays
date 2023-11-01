# Metpy Monday
# 112 - What is 1 - 0.5? Testing Calculations!
# https://www.youtube.com/watch?v=_8Cke2YGDx4

import pytest

import numpy as np

from numpy.testing import assert_almost_equal

from mylib import wind_speed

def test_one_minus_half():
	""" See if basic math holds. """
	# Setup
	truth = 0.5
	
	# Exercise
	result = 1 - 0.5
	
	# Verify
	assert truth == result
	
	# Cleanup

@pytest.mark.skip(reason = "better way to deal with testing this used.")	
def test_one_minus_root_two():
	""" See if more complex math holds. """
	# Setup
	truth = 0.293
	
	# Exercise
	result = 1 - 0.707
	
	# Verify
	assert np.abs(truth - result) < 0.001
	
	# Cleanup
	
def test_one_minus_root_two_better():
	""" Use a better way to test floats. """
	# Setup
	truth = 0.293
	
	# Exercise
	result = 1 - 0.707
	
	# Verify
	assert_almos_equal(truth, result)
	
	# Cleanup
	
def test_wind_speed():
	""" Basic test of the wind speed function. """
	# Setup
	u = 10
	v = 10
	truth = 14.1421
	
	# Exercise
	result = wind_speed(u, v)
	
	# Verify
	assert_almost_equal(truth, result, 3)
	
	# Cleanup


	
	
