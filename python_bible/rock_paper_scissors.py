import random
import sys

choices = ['rock', 'paper', 'scissors']

def welcome_message():
	print("============================================")
	print("=========== Rock-Paper-Scissors ============")
	print("============================================")

welcome_message()

while True:
	def play_game():
		while True:
			player_1 = input("Player1 please choose either rock, paper or scissors: ").strip().lower()
			computer = random.choice(choices)
			print()
			print("Good luck player 1")
			print()
			print("computer has chosen {}".format(computer))
			print()
			if player_1 == computer:
				print("The game is a draw")
				break
			elif player_1 == "rock" and computer == "scissors":
				print("Player1 is the winner, well done!!")
				break
			elif player_1 == "scissors" and computer == "rock":
				print("The computer is the winner, better luck next time")
				break
			elif player_1 == "scissors" and computer == "paper":
				print("Player1 is the winner, well done!!")
				break
			elif player_1 == "paper" and computer == "scissors":
				print("The computer is the winner, better luck next time")
				break
			elif player_1 == "paper" and computer == "rock":
				print("Player1 is the winner, well done!!")
				break
			elif player_1 == "rock" and computer == "paper":
				print("Unlucky the computer is the winner, better luck next time")
				break

	def play_again():
		message = input("Would you like to play again[y/n]? ")
		if message == 'n':
			sys.exit(-1)

	play_game()
	play_again()
