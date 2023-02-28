#!/usr/bin/env python

# Metpy Monday
# 60 - Scripting Part 1
# https://www.youtube.com/watch?v=PzKzlelmEkE

import time

print('Beginning of my Python script')
for i in range(10, 0, -1):
	print('Launch in {}'.format(i))
	time.sleep(1)
print('Blast-off!')

# Run script: $python metpyMonday60.py or $chmod +x metpyMonday.py $./metpyMonday60.py


