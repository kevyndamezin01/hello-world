import csv
import time
import matplotlib.pyplot as plt
import time
import random

def print_number(seconds):
    listx = []
    uptime = []
    for i in range(seconds):
        result = random.randint(1,20)
        print("Result is: {value}".format(value=result))
        listx.append(result)
        current_time = time.time()
        uptime.append(current_time)
        time.sleep(1)
        create_csv(listx, uptime)
        
        
    return listx, uptime

def print_numberx2():
	listy = []
	for i in range(10,20):
	    listy.append(i)

	return listy

def create_csv(listx, uptime):
    with open('mycsv.csv', 'wb') as f:
        thewriter = csv.writer(f, quoting=csv.QUOTE_ALL)
        thewriter.writerow([listx, uptime])

def print_csv():
	f = open('mycsv.csv')
	csv_f = csv.reader(f)

	for row in csv_f:
		print(row)


def plot_csv():
	print("Plotind data from CSV file.")
	f = open('mycsv.csv')
	csv_f = csv.reader(f)	
        x = []

	for row in csv_f:
		fig = plt.figure()
		fig1 = fig.add_subplot(211)

		fig1.plot(row, 'ro')
		plt.show()

		fig.savefig("test.pdf", bbox_inches = 'tight')

print_number(5)
print_csv()
plot_csv()


