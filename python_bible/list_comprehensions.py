even_numbers = [x for x in range (1,100) if x % 2 ==0]
print(even_numbers)

# Here we have a variable called x which is going to loop through the range of,
# 1 - 100 and x will only be stored if x is an even numberself.

odd_numbers = [x for x in range (1,100) if x % 2 !=0]
print(even_numbers)
# This is how we would do it for odd numbers, x would only be stored if x is,
# not an even number.

words = ["The", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
answer = [[w.upper(), w.lower(), len(w)] for w in words]
print(answer)

# Here we have created a list and then created, we then create a second list,
# that will and set it to the variable w inside the top list, it will then go,
# through each word in the list and print out the upper case of the word, lower,
# case of the word and the length of the word.
