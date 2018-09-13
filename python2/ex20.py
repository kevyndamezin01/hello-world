from sys import argv
#Here it is calling for a file, depending on what file you state here is what
#Will be printed out in the terminal
script, input_file = argv

#Here we are calling a fucntion, by putting the (f) in allows you to call the
#Function anywhere in the script by using f
def print_all(f):
#Here by using the f.read() it means it will read the script an print it out in
#The terminal when it is called
  print f.read()

#By using the f.seek(0) this will put the file that you have requested to open
#Back up to the start of the file. Each time you do f.seek(0) you are moving to
#The start of the file
def rewind(f):
  f.seek(0)

#Here we are calling a fucntion that is going to print a single line of the
#Off the the file that is inside txt, you call each line by using the line_count
#As this will count each line
def print_a_line(line_count, f):
  print line_count, f.readline()

#Here we are calling to open the file that you have called to open.
current_file = open(input_file)

print "First let's print the whole file:\n"

#Here we are calling to print the whole file
print_all(current_file)

print "Now let's rewind, kind of like a tape."

#Here we are calling to 'rewind' the script basically put the txt file back
#To the start of that file
rewind(current_file)

print "Let's print three lines:"

#Here we are setting current line to 1 which will allow us to print the number 1
current_line = 1
#Here we are calling the print_a_line Function which is going to allow us to
#Print single lines. By adding in the current_line this will print the number of
#The line that we are printing from the file.
print_a_line(current_line, current_file)

#Here we are doing the above but adding in the + 1 which will increase the line
#Count number when it is printed out in the terminal
current_line += current_line
print_a_line(current_line, current_file)

#Here we are doing the above but adding in the + 1 which will increase the line
#Count number when it is printed out in the terminal
current_line += current_line - 1
print_a_line(current_line, current_file)
