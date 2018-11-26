import serial
import matplotlib.pyplot as plt
import time

def open_serial_conection():
	port = serial.Serial('/dev/tty.usbmodem14201', baudrate=115200)

def log_temperature_for_x_seconds(open_serial_conection, time):
	port.flush()
	port.write("get temp")
	time.sleep(1)
	port.readline()

def logged_temperature():	
	logged_temps = log_temperature_for_x_seconds(open_serial_conection, 5)
	temps_int = map(int, logged_temps)
	print(temps_int)



open_serial_conection()
log_temperature_for_x_seconds(op, 5)
logged_temperature()

plt.plot([1,2,3,4,5], temps_int)
plt.show()
