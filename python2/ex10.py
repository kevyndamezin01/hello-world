# By adding in the \t it tabs in on the treminal of what you want to print
tabby_cat = "\tI'm tabbed in."
# By adding in the \non it puts a spilt between the sentence.
persian_cat = "I'm split\non a line."
# By putting in the \\ it print's out a single \
backlash_cat = "I'm \\ a \\ cat."

#Here by adding in the \t* this is tabbing the word out and adding an * to the start of it
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""
print tabby_cat
print persian_cat
print backlash_cat
print fat_cat

while True:
    for i in ["/", "-", "|", "\\", "|"]:
        print "%s\r" % i,

big_cat = '''
This will print out:
\t* The cat is %d cm long which is \"long\" for a cat % 10
\t* The cat is very\non\t* long
'''
print big_cat
