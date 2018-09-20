# A not statment will print the oposite from its true value
# Example not True would print Flase

x = 10
y = 20

# When running this if statment it should return "It worked"
# But because we used a not statment it will return the oposite
# Which would be "It did not work"
if not y > x:
    print("It worked")
else:
    print("It did not work")

# This is how you use the and function
c = 10
d = 5

# For this statment to return the print function both of the
# Statments in the if function both need to return ture else
# This code will not run
if c > 10 and d > 1:
    print("It worked")
else:
    print("It did not work")

# This is how you can incorpirate the if and the and statment
if not(c > 10 and d > 1):
    print("It worked")

# This is the or operiator
c = 5
d = -1

#This statment will print out if either of the inputs are true
if c > 1 or d > 1:
    print("It worked!")

# The only way this will not print is if both of the statments
# are fasle
#if c > 100 or d > 100:
#    print("It worked")

# This is how you incorpirate both not and or to make a nor gate
if not(c > 100 or d > 100):
    print("It worked")

# Complex Example
c = 6
d = 2

# This will print out due to the or gate being there and the first
# Statment showing flase but the second statment is true and as
# It is an or gate the statment will print out true
if (c > 5 and d > 5) or (c > 1 and d > 1):
    print("It worked!!")
