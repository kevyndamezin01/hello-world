# This is how you create a list using []
our_list = [27,46,-5,17,99]
print(type(our_list))

# List can contain both strings and integers (words and numbers)
my_list = ["A","B","C",1,2,3]
print(my_list)

# Each item in the list has an index number.
# You are able to access them by doing the following.
# This will print "1"
print(my_list[3])
# This will print "B"
print(my_list[1])

# You can take out eliments and make them a variable
x = my_list[1]
print(x)

# This is the format to take more than one item out of the list
# my_list[start:end:step]
print(my_list[0:3])

# You are able to have a list inside a List
our_list = [1,2,[3,4,5],6,7,8]
# This will print out the secondary list that is inside the list
print(our_list[2])
# To get a single index from the secondary list you would:
print(our_list[2][0])
print(our_list[2][2])
print(our_list[3])

# This is an example where you have 3 seperate lists inside a list
our_table = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
print(our_table[0])
print(our_table[1])
print(our_table[2])
# As you can see we have 3 lists which means we will need to have Two
# Cordinates to call for a single index
print(our_table[0][2])
print(our_table[1][0])
print(our_table[2][1])
