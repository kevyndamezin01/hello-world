import random
import time 
import subprocess
import sys 
import matplotlib.pyplot as plt

start = time.time()

period_of_time = 120 #2mins

def collect_data(seconds):
	results = []
	print "Collecting Data"
	for s in range(seconds):
		result = random.randint(1,20)
		results.append(result)
		time.sleep(1)
	print "Finished collecting data"
	return results

def print_data(seconds):
	logged_data = collect_data(60)
	print logged_data
	uptime = range(0,seconds)
	print(uptime)
	plt.plot(uptime, logged_data)
	plt.show()

print_data(60)


#while True:
#	results = {'number': [], 'uptime_list': []}
#	result = random.randint(1, 9)
#	uptime = uptime + 1
#	results['number'].append(result)
#	results['uptime_list'].append(uptime)
#	time.sleep(1)

#	if time.time() > start + period_of_time : break
	

def print_numbers():
	start = time.time()
	period_of_time = 60
	while True:
		print(random.randint(1,9))
		time.sleep(1)
		if time.time() > start + period_of_time : break



