#These are all your variables that you have created, to do this you call something and then
#set it equal to a value and then that will allow you to call that variable anywhere.

cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passenger_per_car = passengers / cars_driven

#Here we are using our variables and calling then into our print function
#By placing the variable outside of the "" that means in the terminal it wll print the value

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today"
print "We have", passengers, "to carpool today"
print "We need to put about", average_passenger_per_car, "in each car"
