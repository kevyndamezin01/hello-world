#Here we are calling a function, by putting in the (a, b) this gives us two
#Variables to use.
def add(a, b):
#Here we are simpily printing out a line.
    print "ADDING %d + %d" % (a, b)
#By returning this it will print out what you wish to return in the terminal
    return float(a + b)

def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return float(a - b)

def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return float(a * b)

def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return float(a / b)

#Here we are making a list of variables, when we add in the add(30, 5) this
#Refers to the add functiont that we have created above and replace the (a, b)
#With the (30, 5). And the same for the rest of the variables.
age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

#Here we are printing out this and it will use the maths that you have deffined
#In each function and print that out in the terminal.
print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

#A puzzle for the extra credit, type it anyway

print "Here is a puzzle"
#As we are calling the age and other functions here that explains to why in the
#Terminal that it prints out as DIVIDING 50 / 2.
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "\nCan you do it by hand?"

print "Here is another puzzle"

puzzle = iq(age, subtract(weight - age, 10))

print "The answer to this is ", puzzle
