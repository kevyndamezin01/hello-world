import csv
import time

def print_number():
    listx = []
    for i in range(0, 10):
        listx.append(i)

    return listx

with open('mycsv.csv', 'wb') as f:
    thewriter = csv.writer(f, quoting=csv.QUOTE_ALL)

    thewriter.writerow(['col1', 'col2', 'col3'])
    thewriter.writerow(['one', 'two', 'three'])
    thewriter.writerows([print_number()])
