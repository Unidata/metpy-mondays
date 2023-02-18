# Metpy Monday
# 127 - Multiprocessing and Managed Dictionaries
# https://www.youtube.com/watch?v=JHfEmXjX0CA


from datetime import datetime
import multiprocessing as mp
from multiprocessing import Manager

import metpy.calc as mpcalc
from metpy.units import units, pandas_dataframe_to_unit_arrays
from siphon.simplewebservice.wyoming import WyomingUpperAir

def calculate_pw(d, station, timestamp):
	""" Calculate the value of PW from sounding. """
	try:
		print(f'Station {station} at {timestamp}')
		df = WyomingUpperAir.request_data(timestamp, station)
		df = pandas_dataframe_to_unit_arrays(df)
		d[station] = mpcalc.precipitable_water(df['dewpoint'], df['pressure'])
	except ValueError:
		print('Data not available')
	
def main():
	manager = Manager()
	results = manager.dict()
	
	pool = mp.Pool(4)
	
	jobs = []
	
	stations = ['OUN', 'LZK', 'OAX', 'ABQ', 'DDC', 'BOU', 'DNR', 'TLH', 'TFX', 'TUS', 'OAK', 'SLE']

	t = datetime(2020, 3, 19)
	
	for station in stations:
		job = pool.apply_async(calculate_pw, (results, station, t))
		jobs.append(job)
		
	for job in jobs:
		job.get()
		
	pool.close()
	pool.join()
	
	print(results)
	
if __name__ == '__main__':
	main()

