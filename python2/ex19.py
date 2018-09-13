# By defining the function here and adding two variables insdie the ()
# This allows you to change the values of these variables throught the script
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheese!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that enough for a party!"
    print "Get a blanket.\n"

print "we can just give the function numbers directly"
# Here we have assinged the function to a set of values, in this case it is
# 20 and 30, as you can see insdie the () this will then assig the values
# Inside the () in function to a variable, eg cheese_count is set to 20
# And by calling the function and then adding in the values it will print out
# All that is inside the function using the variables.
cheese_and_crackers(20, 30)

# Here is another way of doing the above.
print "OR, we can use variables fromm our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# Here is doing the same as the others although using math as the value.
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

def amount_of_animals(cats, dogs, fish):
    print "You have %d amount of cats" % cats
    print "You also have %d amount of dogs" % dogs
    print "And finally you have %d amount of fish" % fish

print "How many pets do you have?"
amount_of_animals(10, 20, 30)

print "Here is another way"
cats = 10
dogs = 20
fish = 30

amount_of_animals(cats, dogs, fish)
