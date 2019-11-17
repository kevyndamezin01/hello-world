import sys
import argparse
import serial
import time
import matplotlib.pyplot as plt

def welcome_message():
    print("====================================================")
    print("=========== ADT7310 Temperature Sensor! ============")
    print("====================================================")
    user = raw_input("Do you want to continue [Y/N]? ").lower()
    if user == 'n':
        print('You have chosen not to continue, ending script!')
        sys.exit(-1)

def print_sensor_id(port):
    port.readline() # Needed to get rid of initial strange value
    print("Retrieving the Sesnor's ID.")
    port.flush()
    port.write("get id\n")
    id = port.readline()
    print('Manufacture ID is: {id}'.format(id=id))

def get_temperature_reading(port):
    print("Collecting a temperature reading")
    port.flush()
    port.write("get temp\n")
    temperature = port.readline()
    print("Temperature Reading is: {temp}".format(temp=temperature))

def eliminate_first_guff_reading(port):
    port.flush()
    port.write("get temp\n")
    port.readline()

def log_temperature_readings(port):
    print("Collecting temperture readings")
    start_time = time.time()
    collection_time = args.duration
    results = []
    max_temp = args.max_temp
    min_temp = args.min_temp
    while (time.time() - start_time) < collection_time:
        port.flush()
        port.write("get temp\n")
        temperature = port.readline()
        if temperature == max_temp or min_temp:
            print("Temperature has hit limit exiting the script.")
            exit(-1)
        print("Temperature Reading is: {temp}".format(temp=temperature))
        results.append(temperature)
    print("Finished collecting temperature readings!")
    return results

def plot_temperature_readings():
    temps = map(int, logged_temps)
    x_axis = temps
    y_axis = range(0, len(temps))
    plt.plot(y_axis, x_axis)
    plt.show()

def print_temperature_readings():
    temps = map(int, logged_temps)
    print("You have chosen not to plot the results")
    print("Temperature readings in Degrees are: {temps}".format(temps=temps))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
    description= """This script will open a serial connection to an arduino which
					will then control a temperature sensor and collect temperature
					reading over a given period.""")
    parser.add_argument("-c", "--com-port", help="Provide the port which the arduino is conected to.",
                        action='store', required=True, type=str)
    parser.add_argument("-d", "--duration", help="Specifiy the amount of time that you wish to collect"
                        "collect temperature readings for", type=int, action='store', default=10, required=False)
    parser.add_argument("-p", "--plot-results", help="Specifiy if you wish to plot the results or not", action='store_true',
                      required=False)
    parser.add_argument("-max", "--max-temp", help="Porvide a max limit for the temperature sensor", action='store',
                        type=int, default=40, required=False)
    parser.add_argument("-min", "--min-temp", help="Provide a minimum limit for the temperature sensor", action='store',
                        type=int, required=False, default=-1)
    args = parser.parse_args()

    welcome_message()

    port = serial.Serial(args.com_port, baudrate=9600)

    eliminate_first_guff_reading(port)

    get_temperature_reading(port) # Needed to get rid of initial false reading

    logged_temps = log_temperature_readings(port)

    if args.plot_results:
        plot_temperature_readings()
    else:
        print_temperature_readings()


