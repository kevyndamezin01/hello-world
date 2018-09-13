from sys import argv

script, filename = argv

print "We are going to open up %s" % filename
print "IF you do not wish to continue on with the script then press CTRL-C"
print "If you wish to continue then press RETURN"

raw_input("So do you ? ")

print "Opening up the file"
target = open(filename, 'w')
print "Turncating the file"

print "Now i am going to ask you three questions..."

line1 = raw_input("What is your favourite colour?: ")
line2 = raw_input("What is your favourite anaimal?: ")
line3 = raw_input("Waht is your favourite food?: ")

print "I am going to do some magic now..."

target.write("I am going to guess that your favourite colour is: ")
target.write(line1)
target.write("\n")
target.write("I am going to guess that your favourite anaimal is: ")
target.write(line2)
target.write("\n")
target.write("I am going to guess that your favourite food is: ")
target.write(line3)
target.write("\n")
target.write("As you can see i have done some magic to get your inputs into this file!!!")

print("\n")
print "And now go and check the document that i have created"
target.close()
