import random

class Pound:
    # Constructor method, note that the word self will be replaced with
    # any object that you make from the class
    def __init__(self, rare=False):

        self.rare = rare

        if self.rare:
            self.value = 1.25
        else:
            self.value = 1.00

        self.colour = "gold"
        self.num_edges = 1
        self.diameter = 22.5 # mm
        self.thickness = 3.15 # mm
        self.heads = True

    def rust(self):
        self.colour = "greenish"

    def clean(self):
        self.colour = "gold"

    def flip(self):
        heads_options = [True, False]
        choice = random.choice(heads_options)
        self.heads = choice

    def __del__(slef):
        print("Coin Spent!")

coin1 = Pound(rare=True)

print(coin1.value)
print(type(coin1))

print(coin1.colour)
# This is how you change the value of the class
coin1.colour = "greenish"
print(coin1.colour)

# You can create a new object although the object will keep the value of the
# Class and not the value of the first object
coin2 = Pound()
print(coin2.colour)

# Using the rare parameter -
coin1 = Pound(rare=True)
coin2 = Pound()

print(coin1.value)
print(coin2.value)

coin2.rust()
print(coin2.colour)

coin1.clean()
coin2.clean()

print(coin1.colour, coin2.colour)

print(coin1.heads)
coin1.flip()
print(coin1.heads)
coin1.flip()
print(coin1.heads)
coin1.flip()
print(coin1.heads)

del coin1
