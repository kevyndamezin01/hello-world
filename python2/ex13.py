#This is importing from the python feature set
#By using this you must pass in 3 arguments when you call for the script
#For example python ex13.py 1st 2nd 3rd
from sys import argv

script, first, second, third = argv

print "What is you're forth variable?"
forth = raw_input()

print "This sctipt is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
print "Your forth variable is", forth
#As you have passed in 3 arguments at the start when calling the script
#You have actually called 4 as ex13.py is classed as the first, the script
#Will replace first with the 2nd argument and second with the 3rd argument
#And third with the 4th argument. If you do not pass these you will get an error
