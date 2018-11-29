import random
import time 
import subprocess
from logger import Logger
import sys 

sys.stdout = Loogger(str('Practice_Date.txt'))
start = time.time()

period_of_time = 120 #2mins

uptime = 1

while True:
	print(random.randint(1, 9), uptime)
	uptime = uptime + 1
	time.sleep(1)

	if time.time() > start + period_of_time : break
	


def print_numbers():
	max_number = 9
	min_number = 1
	start = time.time()
	period_of_time = 60
	while True:
		print(random.randint(1,9))
		time.sleep(1)
		if print_numbers == max_number : break
		if print_numbers == min_number : break
		if time.time() > start + period_of_time : break

while print_numbers() == True:
	max_number = 9
	min_number = 1
	if print_numbers == max_number : break
	if print_numbers == min_number : break

