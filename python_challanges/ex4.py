number = int(raw_input("Please enter a number: "))

list = range(1, number+1)

for i in list:
    if number % i == 0:
        print i
