import csv
import time
import matplotlib.pyplot as plt

def print_number():
    listx = []
    for i in range(0, 10):
        listx.append(i)

    return listx

def print_numberx2():
	listy = []
	for i in range(10,20):
	    listy.append(i)

	return listy

with open('mycsv.csv', 'wb') as f:
    thewriter = csv.writer(f, quoting=csv.QUOTE_ALL)
    thewriter.writerows([print_numberx2()])
    thewriter.writerows([print_number()])


f = open('mycsv.csv')
csv_f = csv.reader(f)

x = []
y = []	

for row in csv_f:
	print(row)
	plt.plot(row, range(0,len(row)))
	plt.show()

