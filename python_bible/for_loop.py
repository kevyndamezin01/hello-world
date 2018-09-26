# This is how we create a for loop, to do this we start with for and then create,
# a variable which will update each time we go through the loop, then had the,
# key word in and then an iterabile (in this case it was range but this can be,
# a list of numbers or strings etc..)
for number in range(1,100):
    print(number)

# a e i o u = Vowels

vowels = 0
consonants = 0

# Here we are creating a for loop that will count the amount of vowels and consonants,
# in a word.
for letter in "Hello":
    # Here we are making an if statment to check if any of the letters in the,
    # word givin in the loop are a vowel
    if letter.lower() in "aeiou":
        # If this is true then it will add 1 onto the vowel variable which was,
        # defined above.
        vowels = vowels + 1
    # We are using an elif statment to check if any of the letters are a space.
    elif letter == " ":
        # If it is true then it will pass and do nothing
        pass
    # Otherwise if none of these statments are true then it will add 1 to the,
    # consonants variable. 
    else:
        consonants = consonants + 1

print("There are {} vowels".format(vowels))
print("There are {} consonants".format(consonants))
