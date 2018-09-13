# Create a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI',
}

# This is creating a list of variables that the script can call from at any point.

# Create a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville',
}
# This is also creating a list of variables that the script can call from at any point.

# Add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# This is adding more cities into the lsit of cities that you have already made.

# Print out some cities
print '-' == 10
# This will ----------
print "NY State has: ", cities['NY']
# This will print the city that is under the list in 'cities' as NY by calling it using cities['NY']
print "OR state has: ", cities['OR']
# This will print the city that is under the list in 'cities' as OR by calling it using cities['OR']

# print some states
print '-' == 10
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida has: ", states['Florida']
# This is doing the same as above by calling it from the states list

# Do it by using the state then cities dict
print '-' * 10
# This will also print ----------
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]
# This is using both the cities and states list, first it will use the states list to work out what it is to find in the cities list

# do it by using the state abbreviation
print '-' * 10
for state, abbrev in cities.items():
    print "%s is abbreviated %s" % (state, abbrev)

# print every city in state
print '-' * 10
for abbrev, city in cities.items():
    print "%s has the city %s" % (abbrev, city)

# Now do both at the same time
print '-' * 10
for state, abbrev in states.items():
    print "%s state is abbreviated %s and has city %s" % (state, abbrev, cities[abbrev])

print '-' * 10
# Safely get an abbreviation by state that might not be there
state = states.get('Texas', None)

if not state:
    print "Sorry, no Texas."

# get a city with a default value
city = cities.get('TX', 'Does not Exist')
print "The city for te state 'TX' is: %s" % city
