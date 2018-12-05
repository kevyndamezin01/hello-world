import serial
import matplotlib.pyplot as plt
import time
import argparse
import sys
from logger import Logger

def welcome_message():
	print "===================================================="
	print "=========== ADT7310 Temperature Sensor! ============"
	print "===================================================="

def print_id(port):
	port.flush()
	port.write("get id\n")
	print port.readline()
	print port.readline()

def log_temperature_for_x_seconds(port, seconds):
	print "Collecting temperature readings"
	results={'temp': [], 'uptime_list': []}
	uptime = 1
	min_temp = args.min_temp
	max_temp = args.max_temp
	for s in range(seconds):
		port.flush()
		port.write("get temp\n")
		time.sleep(0.1)
		temperature = prot.readline()
		if temperatue <= min_temp:
			port.close()
			print "Ending script minimum temperatue has been reached: " + temperature
			break
		elif temperatue >= max_temp:
			port.close()
			print "Ending script maximum temperature has been reached: " + temperature
			break
		results['temp'].append(temperatue)
		float(uptime)
		results['uptime_list'].append(float(uptime))
		uptime = float(uptime) + 1
		time.sleep(1)
	print "finished collecting temperature readings"
	return results

def uptime():
	uptime = 1
	uptime = uptime + 1
	time.sleep(1)

def print_data(port):
	port.flush()
	port.write("get temp\n")
	temperature = port.readline()
	print "Temperature reading in degrees: " + temperature

def print_temperature():
	logged_temps = log_temperature_for_x_seconds(port, 5)
	temps_int = map(int, logged_temps['temp'])
	uptime_int = logged_temps['uptime_list']
	print "Temperature readings in degrees " + temps_int
	print uptime_int
	graph = {'temp': temps_int, 'uptime': uptime_int}
	return graph

def plot_temperature():
	plt.plot(graph(['uptime']), graph(['temp']))
	plt.show()

if __name__ == '__main__':
	parser = argparse.ArgumentParser(
		description="This script will open a serial connection to an arduino which "\
					"will then control a temperature sensor and collect temperature "\
					"reading over a given period.")
	parser.add_argument("-n", "--num-samples", help="Provide how many temperature readings you would like a second.",
					    action='store_true', required=True)
	parser.add_argument("-d", "--duration", help="Provide how long you would like to collect temperature readings for.",
						action='store_true', required=True)
	parser.add_argument("-p", "--port", help="Provide the port which the arduino is conected to.", action='store_true',
						required=True)
	parser.add_argument("-max", "--max-temp", help="Provide the max temperature that will stop the test if this value is "\
	 					"and is read from the sensor", action='store_true', required=False)
	parser.add_argument("-min", "--max-temp", help="Provide the max temperature that will stop the test if this value is "\
	 					"and is read from the sensor", action='store_tue', required=False)
	parser.add_argument("-f", "--filename", help="Provide a filename for the output log", action='store_tue', required=False,
						type=str)
	parser.add_argument("-p", "--plot-temps", help="Specifiy wether you want the temperature readings plotted to a graph",
						action='store_true', required=Flase)
	args = parser.parse_args()

if args.plot_temps:
	sys.stdout = Loogger(str(args.filename) + 'Temperature readings log')

welcome_message()
port = serial.Serial(args.port, baudrate=115200)

print port.readline()
print port.readline()
print port.readline()

print_id(port)
print_data(port)
print_temperature()

if args.plot_temps():
	plot_temperature()

port.close()
