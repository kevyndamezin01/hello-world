numbers = [1, 2, 3, 4, 5]
print(numbers)

lucky = input("Hello! Is you're lucky number in this list of numbers? [y/n]: ").strip().lower()
if lucky == "y":
    print("Amazing!!")
elif lucky == "n":
    add = input("Would you like to add your lucky number to the list? [y/n]: ").strip().lower()
    if add == "y":
        user_number = input("Please enter your lucky number: ").strip()
        numbers = numbers + [user_number]
        print(numbers)

name = input("What is you're name i would like to add it to the list?: ")
numbers = numbers + [name]
print(numbers)
print("I am now going to add your name in by each single letter!")
numbers = numbers + list(name)
print(numbers)

# This script is to demostrate that there is other ways to add to a list without using .append()
# We can add to a list by following this format list = list + [1]. This is how we would add a
# Number to a list, we can also follow the same format to add in a string list = list + [a].
# We can also do list = list + list(kevyn) and in the output it would add kevyn by each
# index rather than a whole word. So it would print out in the output as: 'k', 'e', 'v'...
# rather than 'kevyn'.
