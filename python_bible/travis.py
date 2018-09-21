known_users = ["Alice", "Bob", "Claire", "Dan", "Emma", "Fred", "Georgie", "Harry"]
# The len function will tell you the length of the list
print(len(known_users))

while True:
    print("Hi! My name is Travis")
    name = input("What is your name?: ").strip().capitalize()
    if name in known_users:
        print("Name recognised")
        print("Hello {}!".format(name))
        remove = input("Woul you like to be removed from the system [y/n]?: ").strip().lower()
        if remove == "y":
            known_users.remove(name)
        elif remove == "n":
            print("No problem, i didn't want you to leave anyway!")
    else:
        print("Hmmmm i don't think i have met you yet {}".format(name))
        add_me = input("Would you like to be added to the system[y/n]?: ").strip().lower()
        if add_me == "y":
            known_users.append(name)
        elif add_me == "n":
            print("No problem, see you around")
# To delet from a list you can eiher use .remove(name) which will delete a specific nameself.
# Or you can use del name[0] and what you put inside the [] is the index number that you wish to delete.
