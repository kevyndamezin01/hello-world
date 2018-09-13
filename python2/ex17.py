from sys import argv
#Exists Test whether a path exists.  Returns False for broken symbolic links
from os.path import exists

#Here we are asking the user for two arguments, 1st what file they wish to
#Open and the second which file they wish to create
script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

# We could do these two on one line too, how?
#Here we are opening up the script that we only wish to read not to edit in
#We do this by using open, we are then calling that we only want to read, what
#Is inside the file not edit the file
in_file = open(from_file)
indata = in_file.read()

#Here we are printing what size the file is, to do this we have used 'len'
#This allows the script to read what size of file indate is and print it out
print "The input file is %d bytes long" % len(indata)

#By using 'exists' this will check if the file exists or not and will return
#True if it does or False if it doesn't
print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input("> ")

#Here we are opening up the file that we wish to add text into.
out_file = open(to_file, 'w')
#By puting the 'indate' isnide the () this will transfer everything that is in
#The file of 'indata' into the new file.
out_file.write(indata)

print "Alright, all done."

out_file.close()
in_file.close()
