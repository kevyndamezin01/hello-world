# For this dictionary the name is the students name and the number is the students
# Age. The name will be the item and the age is the value. This is the format you
# should follow for creating a dictionary. You do not need to have both string
# and integer in the dictionary
students = {"Alice":25, "Bob":27, "Clare":17, "Dan":21, "Emma":22}
print(students)
# This has looked through the dictionary and found the key of "Dan" and returned
# the value (in this case it has returned the age)
print(students["Dan"])

# This is how you add into the dictionary, this will add in the new key to the
# end of the dictionary, the format you follow is to set the key to the value
# and this will add in both the key and the value to the dictionary
students["Fred"] = 25
print(students["Fred"])

# In this example it shows that the values can be changed at any point in the script.
print(students["Alice"])
students["Alice"] = 26
print(students["Alice"])

# This is how you delete a key inside the dictionary. When you delete a key it
# will also delete any values that are assosiated with that key.
print(students)
del students["Fred"]
print(students)


# Note that in a dictionary the only way to gain asccess to a variable is by
# calling it by the key, you cannot call an index
