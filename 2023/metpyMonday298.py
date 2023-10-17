# Metpy Monday
# 298 - Creating Executables with pyinstaller
# https://www.youtube.com/watch?v=IVObcP-KEu4

# install with conda: $conda install -c conda-forge pyinstaller
# intall with pip: $pip install pyinstaller
# save as simple_script.py
# $pyinstaller simple_script.py
# run $./dist/simple_script/simple_script.exe

import matplotlib.pyplot as plt
import numpy as np

while(True):
	exponent = input('Enter an exponent (q to quit): ')
	if exponent == 'q':
		sys.exit()
	else:
		exponent = float(exponent)
	x = np.arange(-100, 100)
	y = x ** exponent
	
	plt.plot(x, y)
	plt.show()
