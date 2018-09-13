from sys import argv

#By using filename as your second variable this allows you to open up the text
#File that you have wrote, but you must call it when you type in your command
#into terminal and it must be the exact name of the file
script, filename = argv

#By calling txt = open(filename) by calling the 'open' this will set txt to the
#file and will allow you to call the context of the file later on in the script
txt = open(filename)

print "Here's your file %r:" % filename
#By calling txt.read() this is going to print out the context of that file.
print txt.read()

filename2 = raw_input("What is your second file name > ")
print "Here is your second file %s:" % filename2
print filename2

print "Type the filename again"
#By putting in the "> " inside the brackets allows it to print out that symbol
#When the script ask's for the value. Here we are re setting the and asking
#for another script that will allow us to print that out when file_again is called
file_again = raw_input("> ")
#Here we are using the txt and open to allow us to open the context of the file
#When it is called to do so
txt_again = open(file_again)

print txt_again.read()
