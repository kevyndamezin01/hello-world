# if statment format - if condition: 'Condition'
if True:
    print("It worked!")

num1 = 100
num2 = 100

if num1 > num2:
    print("Number One if larger than Number Two")
# An elif statment cannot come after a else statment
elif num2 > num1:
    print("Number Two is larger than Number One")
else:
    print("Neither of these numbers are bigger than the other")
