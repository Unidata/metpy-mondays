# Metpy Monday
# 139 - Uploading Plots to S3 from Python Part 2
# https://www.youtube.com/watch?v=4dNDXyVYio8

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


def upload_figures_to_s3(path_to_files, extension, bucket_key, secret_key, bucket_name):
	s3 = boto3.client('s3', aws_access_key_id = bucket_key, aws_secret_access_key = secret_key)
	# Find the files we want to upload
	files_to_upload = list(path_to_files.glob(f'*.{extension}'))
	
	upload_success = True
	for file in files_to_upload:
		try:
			s3.upload_file(str(file), bucket_name, str(file.name))
		except:
			upload_success = False
	return upload_success
	

status = upload_figures_to_s3(Path('plots'), 'png', ACCESS_KEY, SECRET_KEY, BUCKET_NAME)
print(status)


