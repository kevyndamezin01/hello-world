import sys
import argparse
import serial
import time
import matplotlib.pyplot as plt
import csv
import os


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


def create_csv(results):
    results_path = "/Users/kevyndamezin/Documents/practice_folder"
    filename = '{}.csv'.format(args.filename)
    with open(os.path.join(results_path, filename), 'wb') as f:
        writer = csv.writer(f)
        writer.writerows([results])


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
        temperature = float(port.readline())
        if temperature == max_temp:
            print("Temperature {temp} has hit max limit {max} exiting the script."
                  .format(temp=temperature, max=max_temp))
            exit(-1)
        elif temperature == min_temp:
            print("Temperature {temp} has hit min limit {min} exiting the script."
                 .format(temp=temperature, min=min_temp))
        print("Temperature Reading is: {temp}".format(temp=temperature))
        results.append(temperature)
    print("Finished collecting temperature readings!")
    print("Putting results into csv file")
    create_csv(results)
    return results


def plot_temperature_readings():
    print("Plotting Temperature Reading that where collected!")
    temps = map(int, logged_temps)
    x_axis = temps
    y_axis = range(0, len(temps))
    plt.plot(y_axis, x_axis, '-x')
    max_temp_limit = args.max_temp
    min_temp_limit = args.min_temp
    if args.max_temp or args.min_tmep in logged_temps:
        plt.axhline(y=max_temp_limit, color='r', linestyle='-')
        plt.axhline(y=min_temp_limit, color='r', linestyle='-')
    else:
        plt.axhline(y=max_temp_limit, color='g', linestyle='-')
        plt.axhline(y=min_temp_limit, color='g', linestyle='-')
    plt.title('ADT7310 Temperature Sensor!')
    plt.xlabel('Temperature (degrees)')
    plt.ylabel('Time (s)')
    plt.show()


def print_temperature_readings():
    temps = map(int, logged_temps)
    print("You have chosen not to plot the results")
    print("Temperature readings in Degrees are: {temps}".format(temps=temps))


if __name__ == '__main__':  
    parser = argparse.ArgumentParser(
             description="""This script will open a serial connection to an arduino which
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
    parser.add_argument("-f", "--filename", help="Provide a Filename in which the CSV file will be saved as",
                        action='store', default="Temperature_Readings")
    args = parser.parse_args()

    welcome_message()

    port = serial.Serial(args.com_port, baudrate=9600)

    eliminate_first_guff_reading(port)

    get_temperature_reading(port)  # Needed to get rid of initial false reading

    logged_temps = log_temperature_readings(port)

    if args.plot_results:
        plot_temperature_readings()
    else:
        print_temperature_readings()


