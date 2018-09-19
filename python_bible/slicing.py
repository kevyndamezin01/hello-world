# Create a variable
word = "supercalifragilisticeexpialidocious"

# For the word above each letter has its own index which starts at 0
print(word[0])
print(word[2])

# General format for slicing = variable[strart:end:step]
# This will print out the word super from the variable above
# It does this by the first number is where you want to start the slice
# The second number is where you want to end the slice
# And the last number is how many eliments you want to go in.
print(word[0:5:1])
print(word[5:9:1])

# This will print from the letter c till the end of the word in a step of 1
print(word[5:])
# This will print from the letter c till the end of the word in a step of 2
print(word[5::2])

# This will allow you to print from the start up to an index
print(word[:8])
print(word[:10])

 #This will print out he word backwards
print(word[::-1])

# You are able to slice backwards by counting using negative numbers
print(word[-1])
print(word[-2])

# This will print out what index number that cali starts at
print(word.index("cali"))

# This will will print out the word cali,
# As it starts by finding the start index of cali and the start index of fragi,
# It will then print out all that is inbtween these two index
print(word[word.index("cali"):word.index("fragi")])

# By adding the : at the end this will print all the index from the start that,
# You have called until the end
print(word[word.index("docious"):])

print(word[0:word.index("docious")])
