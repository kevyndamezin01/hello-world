print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \nnewlines and \t tabs.'

#Here we are printing everything that is inside the speach marsk, using /t will
#tab that line out in the terminal, \n will take a new line.
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \nthe needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""
print "--------"
#Here we are printing everything that we have assigned to print
print poem
print "--------"

five = 10 - 2 + 3 - 6
print "This should be five %s" % five

#Here we have defined a fuction and at the end we have retunred to so that we
#Can use that function later on
def seceret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

start_point = 10000
beans, jars, crates = seceret_formula(start_point)

print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, %d crates." %(beans, jars, crates)

start_point = start_point / 10

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d creates." % seceret_formula(start_point)
