countries = {
        'Scotland': 'SCL',
        'England': 'ENG',
        'Wales': 'WL',
        'Nothern Ireland': 'NL',
}

cities = {
     'GL': 'Glasgow',
     'LN': 'London',
     'BG': 'Bangor',
     'BF': 'Belfast',
}

print countries
print cities

cities['ED'] = 'Edinburgh'
cities['MC'] = 'Manchester'

print '-' * 10
print cities

countries['Dublin'] = 'DB'
countries['France'] = 'FR'

print '-' * 10

print "I am from %s, the capital of %s is %s" % (countries['Scotland'], countries['Scotland'], cities['ED'])

for countrie, abbrev in countries.items():
    print "I am from %s and it is abbreviated to %s" % (countrie, abbrev)

print '-' * 10

for city, abbrev in cities.items():
    print "I am from %s and it is abbreviated to %s" % (city, abbrev)

print '-' * 10

for countrie, abbrev in countries.items():
    print "%s is the abbreviation of %s" % (abbrev, countrie)
