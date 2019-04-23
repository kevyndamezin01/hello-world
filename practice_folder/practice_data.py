import random
import time 
import subprocess
import sys 
import matplotlib.pyplot as plt
sys.path.append('/Users/kevyndamezin/Documents/')
from logger import Logger 

start = time.time()

period_of_time = 120 #2mins

max_number = 101
min_number = 0

def collect_data(seconds):
	results = []
	print "Collecting Data"
	for s in range(seconds):
		result = random.randint(1,100)
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
	logged_data = collect_data(seconds)
	uptime = range(0,seconds)        
	fig = plt.figure()
	fig1 = fig.add_subplot(211)
	fig1.plot(uptime, logged_data, 'ro')
	plt.title('Practice Data Graph')
	plt.xlabel('Number of samples collected')
	plt.ylabel('Value of data')
	fig.savefig("practice_data.pdf", bbox_inches = 'tight')
	plt.show()

#sys.stdout = Logger(str('Practice Date Test Output'))

print_data(10, 10)

sys.exit()



