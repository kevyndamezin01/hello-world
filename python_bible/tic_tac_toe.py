import os


board = [" " for i in range(9)]

def print_board():
	row1 = "| {} | {} | {} |".format(board[0], board[1], board[2])
	row2 = "| {} | {} | {} |".format(board[3], board[4], board[5])
	row3 = "| {} | {} | {} |".format(board[6], board[7], board[8])

	print()
	print(row1)
	print(row2)
	print(row3)
	print()

print_board()
os.system('clear')


def player_move(icon):
	if icon == "X":
		number = 1
	elif icon == "O":
		number = 2
	print("You're turn player {}".format(number))
	choice = int(input("What move would you like to enter (1-9)? ").strip())
	if board[choice - 1] == " ":
		board[choice - 1] = icon
	else:
		choice = int(input("Sorry that space is taken please choose again: ").strip())
		board[choice - 1] = icon

def is_victory(icon):
	if (board[0] == icon and board[1] == icon and board[2] == icon) or \
	   (board[3] == icon and board[4] == icon and board[5] == icon) or \
	   (board[6] == icon and board[7] == icon and board[8] == icon) or \
	   (board[0] == icon and board[3] == icon and board[6] == icon) or \
	   (board[1] == icon and board[4] == icon and board[7] == icon) or \
	   (board[2] == icon and board[5] == icon and board[8] == icon) or \
	   (board[0] == icon and board[4] == icon and board[8] == icon) or \
	   (board[2] == icon and board[4] == icon and board[6] == icon):
	   return True
	else:
		return False

def is_draw():
	if " " not in board:
		return True
	else:
		return False

def welcome_message():
	message = """
	      *********************************
                        Tic-Tac-Toe
              *********************************
              """
	print(message)


welcome_message()

while True:
	print_board()
	player_move("X")
	os.system('clear')
	welcome_message()
	print_board()
	if is_victory("X"):
		print("Congradulations player X you have won!!")
		break
	elif is_draw():
		print("There are no winners game is a draw!")
		break
	player_move("O")
	os.system('clear')
	welcome_message()
	if is_victory("0"):
		print_board()
		print("Congradulations O you have won!!").format(number)
		break
	elif is_draw():
		print("There are no winners game is a draw!")
		break
