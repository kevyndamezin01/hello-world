import random
import time 
import subprocess
import sys 
import matplotlib.pyplot as plt
from logger import Logger

sys.path.append('/Users/kevyndamezin/Documents/')
from logger import Logger 

start = time.time()

period_of_time = 120 #2mins

def collect_data(seconds):
	results = []
	print "Collecting Data"
	for s in range(seconds):
		result = random.randint(1,20)
		print result
		results.append(result)
		time.sleep(1)
	print "Finished collecting data"
	return results

def print_data(seconds):
	logged_data = collect_data(60)
	print logged_data
	uptime = range(0,seconds)
	plt.plot(uptime, logged_data)
	plt.title('Practice Data Graph')
	plt.xlabel('Number of samples collected')
	plt.ylabel('Value of data')
	plt.show()

sys.stdout = Logger(str('Practice Date Test Output'))

print_data(60)

sys.exit()



