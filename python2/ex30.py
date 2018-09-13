the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

#This first kind of for-lop goes through a list

# By saying for number this will then go into the list that you have created
# And assign each variable in that list as a location.
for number in the_count:
# By saying print it will print your statment and then add in the first variable
# Of the list that you have stated and then do so for there of the list.
    print "This is count %d" % number

# same as above
for fruit in fruits:
    print "A fruit of type: %s" % fruit

# Also we can go through mixed lists to
# Notice we have to use %r since we don't know what's in it
# We have to use %r here as there are integers and string in this list.
for i in change:
    print "I got %r" % i

# We can also build lists, first start with an empty one
elements = []

# Then use the range function to do 0 to 5 counts
# By using range and putting what numbers you wish to add into the list this
# This will add these into the list. To add them you must do and .append()
for i in range(0, 6):
    print "Adding %d to the list." % i
    # append is a function that lists understand
    elements.append(1)

# Now we can print them out too
for i in elements:
    print "Element was: %d" % i
