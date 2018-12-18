import random
import time 
import subprocess
import sys 
import matplotlib.pyplot as plt

sys.path.append('/Users/kevyndamezin/Documents/')
from logger import Logger 

start = time.time()

period_of_time = 120 #2mins

max_number = 21
min_number = 0

def collect_data(test, seconds):
	for t in range(test):
		results = []
		print "Collecting Data"
		for s in range(seconds):
			result = random.randint(1,20)
			print 'Data collected is: ' + str(result)
			results.append(result)
			time.sleep(1)
			if result >= max_number:
				print 'Max Value has been reached ' + str(result)
				sys.exit()
			elif result <= min_number:
				print 'Min Value has been reached ' + str(result)
				sys.exit()
		print "Finished collecting data"
	return results

def print_data(test, seconds):
	logged_data = collect_data(60, 5)
	print logged_data
	uptime = range(0,seconds)
	plt.plot(uptime, logged_data)
	plt.title('Practice Data Graph')
	plt.xlabel('Number of samples collected')
	plt.ylabel('Value of data')
	plt.show()

sys.stdout = Logger(str('Practice Date Test Output'))

print_data(60, 5)

sys.exit()



