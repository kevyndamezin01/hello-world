i = 0
numbers = []

# Starting with while starts the loop. And here we are giving it a regulation
# By saing while it is less then 6 so this.
while i < 6:
    print "At the top i is %d" % i
# By using the .append this will allow us to add numbers.
    numbers.append(i)

    i = i + 1
# Here we are telling it what to do by using the .append now this will add
# What ever the value of i is to the numbers which we have called above.
    print "Numbers now:", numbers
# Now we are printing another variable by using what we have called i above
# Since this is a while function this will carry this out untill i is no longer
# Bellow the value of 6
    print "At the bottom i is %d" % i

print "The numbers: "

# Here we are talking the values that is in numbers and printing them.
for num in numbers:
    print num
