import random
import time 
import subprocess

start = time.time()

period_of_time = 120 #2mins

uptime = 1

while True:
	print(random.randint(1, 9), uptime)
	uptime = uptime + 1
	time.sleep(1)

	if time.time() > start + period_of_time : break
	
