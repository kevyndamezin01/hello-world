#Here we are calling a variable and in that variable we are using the %d to call a string
#These functions will then be called on later in the script
x = "There are %d types of people." % 10 #1
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s" % (binary, do_not)

#We are now calling the above fucntions and printing them
print x
print y

#We are now calling the functions again but putting them into text
#We are using the %r and %s as it makes the code look alot neater rather than calling the function
print "I said: %r." % x #2
print "I also said: '%s'." % y

#Here we are calling two more functions
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

#Here is another way to call two functions if one is either true or false
print joke_evaluation % hilarious #3

#Here is another two functions
w = "This is the left side of..."
e = "a string which a right side."

#Here we are simpily calling and printing both fucntions by using the +
print w + e #4
