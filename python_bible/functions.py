# Def tells python we are defining a function,
# Addition is the function name,
# Whatever is inside the brackets are the paramaters.
def addition(a,b):
    return a + b


# Here we need to call the function and add in the paramaters,
# We wish to use.
print(addition(10,5))

# By using return instead of print this will allow the user to store,
# the variable later on in the script, using the print function,
# this will not allow you to do this.

word = "pen"
# This will print the word backwards
print(word[::-1])

def rev(text):
	word = text
	return word[::-1]

print(rev("kevyn"))

def backwards():
	word = input("Please enter a sentance you would like to be returned backwards: ").strip().lower()
	return word[::-1]

print(backwards())

# By passing arguments inside the () this makes them requirement argruments,
# This means that they must be passed in order for the function,
# to be run.

def about(name, age, likes):
	sentence = "Meet {} they are {} years old and they like {}".format(name, age, likes)
	return sentence

print(about("kevyn", 20, "Python"))

# You can assign the requirement arguments a default value which measns,
# you do not need to pass it when you are calling the function.

def about(name = "Kevyn", age = 21, likes = "Python", haircolor = "Brown"):
	sentence = "Meet {} they are {} years old and they like {} and has {} hair".format(name, age, likes, haircolor)
	return sentence

print(about())

#########################################################################

print(1,2,3,4,5)

numbers = [1,2,3,4,5]
print(numbers)

# By adding in the * this unpacks the list, This will make each item in the,
# list its own argument
print(*numbers)

def add(x,y):
	return(x + y)

print(add(10,20))


def add(*numbers):
	total = 0
	for number in numbers:
		total = total + number
	return(total)

print(add(1,2,3,4,5,6,7,8,9))


def about(name, age, likes):
	sentence = "Meet {} They are {} years old and they like {}".format(name, age, likes)
	return sentence

dictionary = {"name": "Kevyn", "age": "21", "likes": "Python"}

# We use one start for normal arguments and we use two start for key work arguments
print(about(**dictionary))


def foo(**kwargs):
	for key, value in kwargs.items():
		print("{}:{}".format(key, value))

print(foo(huda = "Female", Kevyn = "male", john = "male"))













