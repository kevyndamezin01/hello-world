import serial
import matplotlib.pyplot as plt
import time
import argparse
import sys
#from logger import Logger

def welcome_message():
	print "===================================================="
	print "=========== ADT7310 Temperature Sensor! ============"
	print "===================================================="
	user = raw_input("Do you want to continue [Y/N]? ").lower()
	if user == 'n':
		print 'You have chosen not to continue, ending script!'
		sys.exit()

def print_id(port):
	print 'Retreving the Manufacturers ID'
	port.flush()
	port.write("get id\n")
	print 'Manufacturer Number: ' + port.readline()

def log_temperature_for_x_seconds(port, seconds, samples):
	print "Collecting temperature readings"
	results = []
	for s in range(seconds):
		port.flush()
		port.write("get temp\n")
		time.sleep(samples)
		temperature = port.readline()
		print 'Temperature in degrees celsius is: ' + temperature
		results.append(temperature)
		time.sleep(1)
		if temperature >= args.max_temp:
			port.close()
			print "Ending script maximum temperature has been reached: " + str(temperature)
			sys.exit()
		elif temperature <= args.min_temp:
			port.close()
			print "Ending script minimum temperature has been reached: " + str(temperature)
			sys.exit()
	print "finished collecting temperature readings"
	return results

def print_data(port):
	port.flush()
	port.write("get temp\n")
	temperature = port.readline()
	print "Temperature reading in degrees: " + str(temperature)

def print_temperature(seconds, samples):
	print 'You have chosen not to plot the temperature'
	logged_temps = log_temperature_for_x_seconds(port, seconds, samples)
	temps_int = map(int, logged_temps)
	print 'Temperature readings in Degrees Celsius: ' + str(temps_int)
	return temps_int

def plot_temperature(seconds, samples):
	logged_temps = log_temperature_for_x_seconds(port, seconds, samples)
	temps_int = map(int, logged_temps)
	print 'Temperature readings in Degrees Celsius: ' + str(temps_int)
	uptime = range(0, args.duration)
	plt.plot(uptime, temps_int)
	plt.title('ADT7310 Temperature Sensor!')
	plt.xlabel('Samples Collected')
	plt.ylabel('Temperature in Degrees Celsius')
	plt.show()
			
if __name__ == '__main__':
	parser = argparse.ArgumentParser(
		description="This script will open a serial connection to an arduino which "\
					"will then control a temperature sensor and collect temperature "\
					"reading over a given period.")
	parser.add_argument("-n", "--num-samples", help="Provide how many temperature readings you would like a second.",
					    action='store', type=float, required=True)
	parser.add_argument("-d", "--duration", help="Provide how long you would like to collect temperature readings for.",
						action='store', type=int, required=True)
	parser.add_argument("-c", "--com_port", help="Provide the port which the arduino is conected to.", action='store',
						type=str, required=True)
	parser.add_argument("-max", "--max-temp", help="Provide the max temperature that will stop the test if this value is "\
	 					"and is read from the sensor", action='store', type=float, required=False)
	parser.add_argument("-min", "--min-temp", help="Provide the max temperature that will stop the test if this value is "\
	 					"and is read from the sensor", action='store', type=float, required=False)
	parser.add_argument("-f", "--filename", help="Provide a filename for the output log", action='store', required=False,
						type=str)
	parser.add_argument("-p", "--plot-temps", help="Specifiy wether you want the temperature readings plotted to a graph",
						action='store_true', required=False)
	args = parser.parse_args()

	#if args.plot_temps:
	#	sys.stdout = Logger(str(args.filename) + 'Temperature readings log')

	welcome_message()
	
	port = serial.Serial(args.com_port, baudrate=115200)

	port.readline()

	print_id(port)
	print_data(port)

	if args.plot_temps:
		plot_temperature(args.duration, args.num_samples)
	else:
		print_temperature(args.duration, args.num_samples)

	port.close()
