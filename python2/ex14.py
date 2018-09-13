from sys import argv

script, user_name,  = argv
#By adding in this prompt and giving it a symbol this allows you to call that
#Where raw_input is being called. This will print the symbol when the script
#Has asked a question
prompt = '> '

#By using the %s this allows you to make the script neater.
print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Is that okay?"
question = raw_input(prompt)

print "Do you like %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print ""

#By using the """ this allows you to type any script into between the two """
#When using the %s inside these you do not call for what you want the %s to be
#Replaced with until the """ has been closed.
print """
Alright, so you said %s about liking me.
You live in %s. Not sure where that is.
And you have a %s computer. Nice.
""" % (likes, lives, computer)
