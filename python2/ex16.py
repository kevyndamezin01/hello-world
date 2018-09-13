from sys import argv

script, filename = argv
#Here we are calling the filename that we have supplied as one of the arguments
#And then supplying print commands to either stop the script or continue on
print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."
#By adding in this line of code it will allow the user to read the print
#Statments that will allow them to decided if they want to continue on with the
#Script or not
raw_input("?")


print "Opening the file..."
#Here we are calling a function that is going to open up the file that and
#Set up the file so that we can write text into that file, we do this by
#Adding in the 'w'
target = open(filename, 'w')
print "Truncating the file, Goodbye!"
target.truncate

print "Now I'm going to ask you for three lines"
#Here we are asking the user to input 3 lines of text that will be written into
#The file that you have created.
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

#By using 'target.write(line1)' this is telling the script that in the file
#Write in line one
target.write(line1 + "\n" + line2 + "\n" + line3)
#By using "\n" this is telling the script to take a new line.
#target.write("\n")
#This is telling the script to write in line2 (The raw_input that you inputed)
#target.write(line2)
#By using "\n" this is telling the script to take a new line.
#target.write("\n")
#This is telling the script to write in line3 (The raw_input that you inputed)
#target.write(line3)
#By using "\n" this is telling the script to take a new line.
#target.write("\n")

print "And finally, we close it."
#By using target.close this means that you are closing the file and will not
#Allow you to make any more changes to the file without re opening the file
target.close()
