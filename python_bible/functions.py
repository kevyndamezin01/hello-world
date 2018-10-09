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