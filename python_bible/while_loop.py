# General Format for a while loop :
# while condition:
#     code.....
# While this condition is true this script will continue to run untill false

# We start with a variable of 1 and the while loop will continue to check that
# that number is less than or equal to 10 and if this is true then it will
# print the number and then add 1 onto th number and continue the process
# untill the loop reaches 10
number = 1

while number <= 100:
    if number % 2 == 0:
        print(number)
    number = number + 1
else:
    print("Number has reached greater than 10")

L = []

while len(L) < 5:
    new_name = input("Please add a new name: ").strip().lower()
    L.append(new_name)
    print(L)
else:
    print("Sorry list is full")

# We can use loops for lists. Here we have a empty list and by saying while then
# list has less than 3 variables ask the user to insert a name that will be saved
# inside the list. Once the list reaches the max of 3 print to say that there
# is no more room.
