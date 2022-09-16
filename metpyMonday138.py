# Metpy Monday
# 138 - Uploading Plots to S3 from Python Part 1
# https://www.youtube.com/watch?v=NemWv_HEd3Y

import numpy as np
import matplotlib.pyplot as plt
import boto3
from pathlib import Path

ACCESS_KEY = ''
SECRET_KEY = ''
BUCKET_NAME = ''

def make_line_plot(slope, intercept):
	x = [-100, 100]
	y = np.polyval([slope, intercept], x)
	plt.clf()
	plt.plot(x, y)
	plt.grid()
	plt.ylim(-1000, 1000)
	plt.savefig(Path('plots') / f'plot_{slope}_{intercept}.png')
	
plots = [(1, 0), (10, 5), (50, 10), (2.5, 6.7)]
for coeff in plots:
	make_line_plot(*coeff)

