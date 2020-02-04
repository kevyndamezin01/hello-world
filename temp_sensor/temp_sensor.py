import serial
import matplotlib.pyplot as plt
import time
import argparse
import sys
import csv


def welcome_message():
	print("====================================================")
	print("=========== ADT7310 Temperature Sensor! ============")
	print("====================================================")
	user = raw_input("Do you want to continue [Y/N]? ").lower()
	if user == 'n':
		print('You have chosen not to continue, ending script!')
		sys.exit(-1)

def print_id(port):
	print('Retreving the Manufacturers ID')
	port.flush()
	port.write("get id\n")
	print('Manufacturer Number: {port}'.format(port=port.readline()))

def create_csv(results):
    with open(args.filename.csv, 'wb') as f:
        write = csv.writer(f)
        write.writerows(results)

def log_temperature_for_x_seconds(port, duration, samples):
	print("Collecting temperature readings")
	results = []
	start_time = time.time()

	while (time.time() - start_time) < duration:
		#print('Current time: {}'.format(time.time()))
		#print('end time: {}'.format(start_time + duration))
		#print('seconds: {}'.format(duration))
		current_time = time.time()
		port.flush()
		port.write("get temp\n")
		temperature = float(port.readline())
		end_time = time.time()
		#print('Exec time: {}'.format(end_time - current_time))
		print('Temperature in degrees celsius is: {}'.format(str(temperature)))
		results.append(temperature)
		time.sleep(samples)
		if temperature >= args.max_temp:
			port.close()
			print("Ending script maximum temperature has been reached: {}".format(str(temperature)))
			sys.exit()
		elif temperature <= args.min_temp:
			port.close()
			print("Ending script minimum temperature has been reached: {}".format(str(temperature)))
			sys.exit()

	print("finished collecting temperature readings")
	create_csv(results)

def print_data(port):
	port.flush()
	port.write("get temp\n")
	temperature = port.readline()
	print("Temperature reading in degrees: {}".format(str(temperature)))

def print_temperature():
	print('You have chosen not to plot the temperature.')
	temps_int = map(int, logged_temps)
	print('Temperature readings in Degrees Celsius: {}'.format(str(temps_int)))
	return temps_int

def plot_temperature():
	temps_int = map(int, logged_temps)
	print('Temperature readings in Degrees Celsius: {}'.format(str(temps_int)))
	uptime = range(0, len(temps_int))
	plt.plot(uptime, temps_int, '-x')
	max_temp_limit = args.max_temp, args.max_temp
	min_temp_limit = args.min_temp, args.min_temp
	if args.max_temp in temps_int:
		plt.plot(max_temp_limit, 'r')
		plt.plot(min_temp_limit, 'r')
	else:
		plt.plot(max_temp_limit, 'g')
		plt.plot(min_temp_limit, 'g')
	plt.title('ADT7310 Temperature Sensor!')
	plt.xlabel('Samples Collected')
	plt.ylabel('Temperature in Degrees Celsius')
	plt.show()
			
if __name__ == '__main__':
	parser = argparse.ArgumentParser(
		description="This script will open a serial connection to an arduino which "\
					"will then control a temperature sensor and collect temperature "\
					"reading over a given period.")
	parser.add_argument("-s", "--samples", help="How long to wait between samples. Minimum is 1.5 seconds.",
					    action='store', type=int, required=False, default=1)
	parser.add_argument("-d", "--duration", help="Provide how long you would like to collect temperature readings for.",
						action='store', type=int, required=False, default=5)
	parser.add_argument("-c", "--com-port", help="Provide the port which the arduino is conected to.", action='store',
						type=str, required=False, default='COM55')
	parser.add_argument("-max", "--max-temp", help="Provide the max temperature that will stop the test if this value is "\
	 					"and is read from the sensor", action='store', type=float, required=False, default=30)
	parser.add_argument("-min", "--min-temp", help="Provide the max temperature that will stop the test if this value is "\
	 					"and is read from the sensor", action='store', type=float, required=False, default=-10)
	parser.add_argument("-f", "--filename", help="Provide a filename for the output log", action='store', required=False,
						type=str)
	parser.add_argument("-p", "--plot-temps", help="Specifiy wether you want the temperature readings plotted to a graph",
						action='store_true', required=False)
	args = parser.parse_args()

	welcome_message()
	
	port = serial.Serial(args.com_port, baudrate=9600)

	port.readline()

	print_id(port)
	print_data(port)

	logged_temps = log_temperature_for_x_seconds(port, args.duration, args.samples)

	if args.plot_temps:
		plot_temperature()
	else:
		print_temperature()

	print("Closing port to the arduino, Goodbye :)!")
	port.close()
