# Metpy Mondays
# 82 - Multiprocessing
# youtube.com/watch?v=i_P98aBiTsg

# 1

import pandas as pd
import numpy as np
from pathlib import Path

import time
start = time.time()

data_path = Path('data')

col_names = ['ID', 'Number', 'Time', 'Relative Humidity', 'Air temperature', 'Windspeed']


mean_values = dict()

for fname in data_path.glob('*.mts'):
	station_means = dict()
	df = pd.read_csv(fname, delim_whitespace = True, skiprows = 3, usecols = range(6), names = col_names)
	
	for column in df.columns:
		if column not in ['ID', 'Number', 'Time']:
			station_means[column] = np.mean(df[column])
	mean_values[df['ID'][0]] = station_means
	
end = time.time()
print(end - start)

# 2 - multiprocessing

import pandas as pd
import numpy as np
from pathlib import Path

def get_station_means(fpath):
	col_names = ['ID', 'Number', 'Time', 'Relative Humidity', 'Air temperature' , 'Windspeed']
	
	station_means = dict()
	df = pd.read_csv(fpath, delim_whitespace = True, skiprows = 3, usecols = range(6), names = col_names)
	
	for column in df.columns:
		if column not in ['ID', 'Number', 'Time']:
			for i in range(1000):
				station_means[column] = np.mean(df[column])
	return [df['ID'][0], station_means]
	
means = dict()
def record_means(res):
	station_id, station_means = res
	means[station_id] = station_means
	
if __name__ = '__main__':
	import time
	start = time.time()
	
	import multiprocessing as mp
	
	data_path = Path('data')
	
	with mp.Pool(processes = 6) as pool:
		for fname in data_path.glob('*.mts'):
			pool.apply_async(get_station_means, args = (fname,), callback = record_means)
		pool.close()
		pool.join()
	
	end = time.time()
	print(end - start)
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
