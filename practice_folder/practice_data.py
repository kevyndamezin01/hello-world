import random
import time 
import subprocess
import sys 
import matplotlib.pyplot as plt

start = time.time()

period_of_time = 120 #2mins

def collect_data(seconds):
	results = {'number': [], 'uptime_list': []}
	uptime = 1
	print "Collecting Data"
	for s in range(seconds):
		result = random.randint(1,9)
		results['number'].append(result)
		uptime
		results['uptime_list'].append(uptime)
		uptime = uptime + 1
		time.sleep(1)
	print "Finished collecting data"
	return results

def print_data():
	number = []
	uptime = []
	logged_data = collect_data(5)
	number.append(logged_data[['number']])
	uptime.append(logged_data[['uptime_list']])
	print number
	print uptime
	plt.plot(uptime, number)
	plt.show()

print_data()


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



