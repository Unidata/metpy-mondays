#!/usr/bin/env python

# Metpy Monday
# 61 - Scripting Part 2
# https://www.youtube.com/watch?v=mbef-FyG3n8

import argparse
import time

parser = argparse.ArgumentParser(description = 'Make a countdown timer to an event')
parser.add_argument('--event', default = 'Blast Off!', help = 'Event message at end of timer.')
parser.add_argument('--start', default = 10, type = int, help = 'Duration of the timer in seconds.')
parser.add_argument('--preamble', default = None, help = 'Pre-countdown message.')
args = parser.parse_args()

if args.preamble:
	print(args.preamble)
	
for i in range(args.start, 0, -1):
	print('Timer expires in {} seconds'.format(i))
	time.sleep(1)
print(args.event)

