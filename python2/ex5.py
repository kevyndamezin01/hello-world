#These are all the variables that i have chosen
my_name = 'Zed A. Shaw'
my_age = 35
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'
my_toes = 'Long'

#%s is for a string
#%d is for an integer
#By putting in the %d and then calling which integer you wish to use at the end it makes the code neater

print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not to heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth
print "He has very %r toes" % my_toes

print "If i add %d, %d, and %d i get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight)
