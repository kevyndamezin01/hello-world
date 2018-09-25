# By adding in the [] this allows you to add a list inside the dictionary
students = {
        "Alice": ["ID0001", 26, "A"],
        "Bob": ["ID0002", 27, "B"],
        "Clare": ["ID0003", 17, "C"],
        "Dan": ["ID0004", 21, "D"],
        "Emma": ["ID0005", 22, "E"]
        }

# By adding the key name and then and index number this will allow you extract
# Specific data from the list
print(students["Clare"][0])
print(students["Dan"])

# We can also add a dictionary inside an dictionary by using {}
students = {
        "Alice": {"id": "ID0001", "age":26, "grade":"A"},
        "Bob": {"id": "ID0002", "age":27, "grade":"B"},
        "Clare": {"id": "ID0003", "age":17, "grade":"C"},
        "Dan": {"id": "ID0004", "age":21, "grade":"D"},
        "Emma": {"id": "ID0005", "age":22, "grade":"E"}
        }

# To print out the values of the dictionaries you follow the bellow format
print(students["Dan"]["age"])
print(students["Emma"]["id"], students["Emma"]["grade"])

# By using dictionaries instead of a list this means that the user does not need
# To know the index numbers of the values. 
