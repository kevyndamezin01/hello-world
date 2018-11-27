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

def log_temperature_for_x_seconds(port, seconds):
	temp = []
	for s in range(seconds):
		port.flush()
		port.write("get temp\n")
		time.sleep(0.1)
		temp.append(port.readline())
	return temp
	print "finished collecting temperature data"

def print_data(port):
	port.flush()
	port.write("get temp\n")
	print port.readline()

def print_temperature():
	logged_temps = log_temperature_for_x_seconds(port, 5)
	temps_int = map(int, logged_temps)
	print(temps_int)

def plot_temperature():
	plt.plot([1,2,3,4,5], temps_int)
	plt.show()


print_id(port)
log_temperature_for_x_seconds(port, 5)
print_temperature()
plot_temperature()

port.close()
