known_users = ["Alice", "Bob", "Claire", "Dan", "Emma", "Fred", "Georgie", "Harry"]
# The len function will tell you the length of the list
print(len(known_users))

while True:
    print("Hi! My name is Travis")
    name = input("What is your name?: ").strip()
    if name in known_users:
        print("name recognised")
    else:
        print("Name NOT recognised")
