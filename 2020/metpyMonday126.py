# - Metpy Monday
# - 126 - Queue with Multiprocessing
# - https://www.youtube.com/watch?v=bgEPYMmGwK0

import multiprocessing as mp
import numpy as np
import time

def writer(q):
	with open('multiprocessing_output.txt', 'w') as f:
		while 1:
			msg = q.get()
			if msg == 'shutdown':
				break
			f.write(msg)
			f.flush()
			
def worker(station, q):
	print(f'Doing work for station {station}')
	time.sleep(5)
	q.put(f'{station}, {np.random.random((1))[0]}\n')
	
def main():
	manager = mp.Manager()
	q = manager.Queue()
	pool = mp.Pool(4)
	
	pool.apply_async(writer, (q, ))
	
	jobs = []
	stations = ['KINX', 'KTUL', 'KBOU', 'KBOS', 'KMIN', 'KMIA', 'KPHL', 'KXNA', 'KSCE', 'KIAD']
	
	for station in stations:
		job = pool.apply_async(worker, (station, q))
		jobs.append(job)
		
	for job in jobs:
		job.get()
		
	q.put('shutdown')
	pool.close()
	pool.join()
	
if __name__ == '__main__':
	main()
	
