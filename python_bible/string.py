x = "Happy Birthday"
print(x)

# This will count how many times a letter appears in you're variable
print(x.count("a"))

# This wll count how many times a word appears in you're variable
print(x.count("day"))

# This will change the variable x to all capital letters
print(x.upper())

# This will change the variable x to all lower case letters
print(x.lower())

# This will change the first letter of the first and second words to a capital letter
print(x.title())

# This will return either true or false if the variable x is all in lower case
print(x.islower())

# This will return either true or false if the variable x is all in capitals
print(x.isupper())

# This will return either if true if the variable is a title else return false
print(x.istitle())

# This will tell us if everything inside the variable is letters
print(x.isalpha())

# This will tell us if everything inside the variable is numbers
print(x.isdigit())

# This will tell us if everything inside the variable is numbers and letters
print(x.isalnum())

# This will tell us how many index a word has. Note this function is case sensitive
print(x.index("Birthday"))

y ="000000happybirthday000000"

# This function will strip away a part of the variable
print(y.strip("0"))

# This function will strip away part of the variable to the right
print(y.rstrip("0"))

# This function will strip away part of the variable to the right
print(y.lstrip("0"))
