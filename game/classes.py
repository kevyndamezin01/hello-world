from sys import exit
from random import randint

class Scene(object):

    def enter(self):
    	print("This scene is not yet configured. Subclass it and implement enter()")
    	exit(1)

class Engine(object):

	def __init__(slef, scene_map):
		self.scene_map = scene_map

	def play(self):
		current_scene = self.scene_map.openning_scene()

	while Ture:
		print("\n--------")
		next_scene = current_scene.enter()
		current_scene = slef.scene_map.next_scene(next_scene_name)

class Death(Scene):

	quips = [
	    "You died. You kinda suck at this.",
	    "Your mom would be proud... if she were smarter.",
	    "I have a small puppy that's better at this."
	]

	def enter(self):
		print Death.quips[randint(0, len(slef.quips)-1)]
		exit(-1)

class Centeral_corridor(Scene):

	def enter(self):
		print "The Gothons of Planet Parcal #25 have invaded your ship and destroyed"
		print "your entire crew. You are the last surviving member and your last"
		print "mission is to get the neutron destruct bomb from the weapon Armory,"
		print "put it in the bridge, and blow the ship up after getting into an"
		print "escape pod."
		print "\n"
		print "You're running down the central corridor to the Weapon Armory when"
		print "a Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown costume"
		print "flowing around his hat filled body. He's blocking the door to the"
		print "Armory and about to pull a weapon to blast you"

		action = raw_input("> ")

		if action == "shoot":
			print "Quick on the draw you yank out you're blaster and fire it at the Gothon."
			print "His clown costume is flowing and moving around his body, which throws"
			print "off your aim. Your laster hits his costume but misses him entirely. This"
			print "completely ruins his brand new costume his mother bought him, which"
			print "makes him fly into a rage and blast you repeatedly in the face until"
			print "you are dead. Then he eats you."

			return 'death'

		elif action == 'dodge':
			print "Like a world class boxer you dodge, weave, slip and slide right"
			print " as the Gothon blaster cracks a laster blast at your head."
			print "In the middle of your artful dodge your foot slips and you"
			print "band your head and pass out."
			print "You wake up shortly after only to die as the Gothon stomps on"
			print "your head and eats you."

			return 'death'

		elif action	== "tell a joke":
			print "Luckly for you they made you learn Gothon insults in the academy."
			print "You tell the one Gothon joke you know:"
			print "LBHE zbgure vf fb sng, jura fur fvgf nebhaq gut uhfr, fur fvgf nebhaq gut ubhfr"
			print "The Gothon stops, tries not to laugh, then bursts out laughing and can't move."
			print "putting him down, then jump through the Weapon Armory door."

			return 'Laser_weapon_armory'

		else:
			print "DOES NOT COMPLITE!"
			return 'Centeral_corridor'

class Laser_weapons(Scene):

	def enter(self):
		pass

class The_bridge(self):

	def enter(self):
		pass

class Escape_pod(self):

	def enter(self):
		pass

class Map(object):

	def __init__(self, start_scene):
		pass

	def next_scene(self, scene_name):
		pass

	def openning_scene(self):
		pass

a_map = Map('Centeral_corridor')
a.game = Engine(a_map)
a.game.play()







