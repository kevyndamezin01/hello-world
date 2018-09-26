# Here we have created a dictionary containing male students names and female,
# students names
students = {
            "male":["Tom", "Charlie", "Harry", "Frank"],
            "female":["Sarah", "Huda", "Samantha", "Emily", "Elizabeth"]
            }

# We have created a for loop that will go into each key of the list which would,
# be male or female.
for key in students.keys():
    # We then made a new for loop and went into each name that is in the key
    # and if the name has an A in it then print the name
    for name in students[key]:
        if "a" in name:
            print(name)
