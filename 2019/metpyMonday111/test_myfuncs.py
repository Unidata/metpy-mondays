from myfuncs import fahrenheit_to_celsius

def test_fahrenheit_to_celsius_freezing():
	""" Test temperature conversion with freezing point of water. """
	# Setup
	temperature_input = 32
	truth = 0
	
	# Exercise
	result = fahrenheit_to_celsius(temperature_input)
	
	# Verify
	assert result == truth
	
	# Cleanup
	
def test_fahrenheit_to_celsius_boiling():
	""" Test temperature conversion with boiling point of water. """
	# Setup
	temperature_input = 212
	truth = 100
	
	# Exercise
	result = fahrenheit_to_celsius(temperature_input)
	
	# Verify
	assert result == truth
	
	# Cleanup
	
	 
