# Here we have imported from the random module the choice function,
# this will choose a random question from the list bellow
from random import choice

# Here we have made a list of questions that the user can be asked
questions = ["Why is the sky blue?: ",
             "Why is a chair called a chair?: ",
             "Why is your hair brown?: "]

# Here we are setting a variable question that the script will choose a random,
# question from the list by using the choice() function.
question = choice(questions)
# Here we will create a variable that will ask the user that question
answer = input(question).strip().lower()

# Here we have created a while statment that will only become false once,
# the user has answered 'just because'
while answer != "just because":
    print(answer)
    answer = input("But why?: ").strip().lower()
else:
    print("Awww okay!")
    exit()
