chickens = 2
cows = 4
pigs = 4

print("This script will tell you how many legs are on the farm")

chicken_amount = int(raw_input("How mnay chickens are on the farm?: "))

cow_amount = int(raw_input("How many cows are on the farm?: "))

pig_amount = int(raw_input("How many pigs are on the farm?: "))

chicken_legs = chickens * chicken_amount
cow_legs = cows * cow_amount
pig_legs = pigs * pig_amount

total_legs = chicken_legs + cow_legs + pig_legs

print("The total amount of legs that are on the farm is {}".format(total_legs))


