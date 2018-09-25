# General Format for a while loop :
# while condition:
#     code.....
# While this condition is true this script will continue to run untill false

# We start with a variable of 1 and the while loop will continue to check that
# that number is less than or equal to 10 and if this is true then it will
# print the number and then add 1 onto th number and continue the process
# untill the loop reaches 10
number = 1

while number <= 10:
    print(number)
    number = number + 1
else:
    print("Number has reached greater than 10")
