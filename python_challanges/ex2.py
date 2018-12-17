choice = int(raw_input("Please enter a number which you would like to check if it is odd or even: "))

def check_number():
	if choice / 2:
		print "{} is a even number".format(choice)
	else:
		print "{} is an odd number".format(choice)

check_number()

num = int(raw_input("Please enter a number of your choice: "))

check = int(raw_input("Please choose a number which you would like to devide your choice above by: "))

def devide_number():
	if num / check == 0:
		print "{} can be devided by {}".format(num, check)
	else:
		print "{} can not be devided by {}".format(num, check)

devide_number()
