#Here we are setting a variable that will allow us to cal this list at a moint
ten_things = "Apples Oranges Cows Telephone Light Sugar"
print ten_things
print "Wait there's not 10 things in that list, let's fix that"

#This is allowing us to seperate each item in the list, so that they can be called on induvidually
stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print "Adding: ", next_one
    stuff.append(next_one)
    print "There's %d items now." % len(stuff)

print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[1]
print stuff[-1] # whoa! Fancy
print stuff.pop()
print ' '.join(stuff) # what? cool!
print '#'.join(stuff[3:5]) # Super cool
