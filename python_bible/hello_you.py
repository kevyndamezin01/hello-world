# Ask user for name
name = input("What is you're name? ")
# Ask user for age
age = input("What age are you? ")
# Ask user for city
city = input("What city do you live in? ")
# Ask user what they enjoy
enjoy = input("What do you enjoy to do? ")
# Create output test
string = '''So you're name is {} and you are {} years old and you live in {} and you enjoy to {}.'''
output = string.format(name, age, city, enjoy)
# Print output to screen
print(output)
