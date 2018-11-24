import random
import time 
import subprocess

start = time.time()

period_of_time = 300 #5mins

while True:
	print(random.randint(1,9))
	time.sleep(1)

	if time.time() > start + period_of_time : break
	f.close()
