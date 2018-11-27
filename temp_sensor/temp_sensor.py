import serial
import matplotlib.pyplot as plt
import time

port = serial.Serial('COM55', baudrate=115200)

print port.readline()
print port.readline()
print port.readline()

def print_id(port):
	port.flush()
	port.write("get id\n")
	print port.readline()
	print port.readline()

def log_temperature_for_x_seconds(port, seconds):
	print "Collecting temperature readings"
	temp = []
	uptime_list = []
	uptime = 1
	for s in range(seconds):
		port.flush()
		port.write("get temp\n")
		time.sleep(0.1)
		temp.append(port.readline())
		uptime
		uptime_list.append(uptime)
		uptime = uptime + 1
		time.sleep(1)
	print "finished collecting temperature data"
	return temp
	return uptime

def uptime():
	uptime = 1
	uptime = uptime + 1
	time.sleep(1)

def print_data(port):
	port.flush()
	port.write("get temp\n")
	print port.readline()

def print_temperature():
	logged_temps = log_temperature_for_x_seconds(port, 5)
	temps_int = map(int, logged_temps)
	print temps_int
	return temps_int

def plot_temperature():
	plt.plot(uptime_list, print_temperature())
	plt.show()


print_id(port)
print_data(port)
print_temperature()
plot_temperature()
port.close()
