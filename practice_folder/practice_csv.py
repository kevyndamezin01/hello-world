import csv
import time
import matplotlib.pyplot as plt
import time
import random

def print_number():
    listx = []
    uptime = []
    for i in range(0, 10):
        result = random.randint(1,20)
        print(result)
        listx.append(result)
        current_time = time.time()
        uptime.append(current_time)
        create_csv(listx, uptime)
        print("Sleeping for 1 second")
        time.sleep(1)
        
        
    return listx

def print_numberx2():
	listy = []
	for i in range(10,20):
	    listy.append(i)

	return listy

def create_csv(listx, uptime):
    with open('mycsv.csv', 'wb') as f:
        thewriter = csv.writer(f, quoting=csv.QUOTE_ALL)
        thewriter.writerows([listx])
        thewriter.writerows([uptime])

def print_csv():
	f = open('mycsv.csv')
	csv_f = csv.reader(f)

	for row in csv_f:
		print(row)


def plot_csv():
	print("Plotind data from CSV file.")
    f = open('mycsv.csv')
    csv_f = csv.reader(f)	

    for row in csv_f:
	    print(row)
	    plt.plot(row, range(0,len(row)), 'ro')
	    plt.show()

print_number()
print_csv()
plot_csv()

