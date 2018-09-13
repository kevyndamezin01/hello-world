people = 30
cars = 40
buses = 15

if cars > people:
    print "We should take the cars."
elif cars < people:
    print "We should not take the cars"

if buses > cars:
    print "That's too many buses"
#Elif means that if the first statment is not true try this
elif buses < cars:
    print "Maybe we could take the bus."
#Else means that if the other statments are not true then DO this, this means
#That it will only check to see if the above statments are true and if they
#Are not then it will print out the statment
else:
    print "We still can't decide."

if people > buses:
    print "Alright, lets just take the bus"
else:
    print "Fine. Let's stay home then"

if people + buses < buses * people:
    print "Then i think it is best that we take the car"
else:
    print "We will need to walk then"
