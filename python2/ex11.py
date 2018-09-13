#By asking for raw_input this means it will ask the user of the script this question
#By adding the , at the end this means it will ask you to put your input on the same lien
print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

#You can use %s here but by using %r it means that it will print it out in ''
print "So you are %r years old, and %r tall, and you are %r heavy" % (age, height, weight)

#This is a new way in you can use raw_input it makes the code neater
#If you do not add the space at the end then it will not leave a space between your input and the question
name = raw_input("What is your name? ")
area = raw_input("Where do you live? ")

print "Hi %s its nice to meet you, i belive that you are %s years old. You live in %s i also live there" % (name, age, area)
