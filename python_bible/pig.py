# get sentence from user
# split sentence into words
# loop through words and conver to pig latin
# if it starts with a vowel add "yay"
# Otherwise, move the first consonants cluster to the end and add "ay"
# stick words back together
# output the final string

original = input("Please enter a sentence that you would like to be translated to pig latin!: ").lower().strip()
# By using the .split() function this will split a string at each word
words = original.split()
# Here we have created an empty list to add in the pig latin words.
new_words = []

# Here we have made a for loop to go through the split words
for word in words:
    # Here we are checking if the first letter in the word is a vowel by using,
    # the [0] index
    if word[0].lower() in "aeiou":
        # if the word is a vowel then add on to the end of the word "yay"
        new_word = word + "yay"
        # And then add it to the empty list of new_words
        new_words.append(new_word)
    # Otherwise
    else:
        # Here we are creating a variable to check for a vowel.
        vowel_pos = 0
        # Here we are using a loop to go through each letter in the word and,
        # check if the where there is a vowel in the word as we know that the,
        # first letter has to be a consonants
        for letter in word:
            if letter not in "aeiou":
                # if the letter is not a vowel then move onto the next letter,
                # until you find a vowel
                vowel_pos = vowel_pos + 1
            else:
                # This break will take us out the loop and put us back in the,
                # else loop above.
                break
        # Here we are using a slice to slcie all the letters up to the vowel,
        # possition as a variable.
        cons = word[:vowel_pos]
        # We are now using a slice to slice all of the letters after and including,
        # the vowel as a variable
        the_rest = word[vowel_pos:]
        # Here we are joining the two words togehter in the order that we want,
        # them to be joined in and adding "ay" at the end of the word.
        new_word = the_rest + cons + "ay"
        # And then add it to the empty list of new_words
        new_words.append(new_word)

# Here we are creating an empty list and using the .join() function to add,
# the list of pig latin words.
output = " ".join(new_words)
print(output)
