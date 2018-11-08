name = input("What is your name?: ").strip().lower()

age = input("Hi there {}, now that i know you're name what age are you?: ".format(name))

print("Okay {} and you are {} years old".format(name, age))

year = (2018 - age * 100)

print(year)