import time
import random

max_number = 9
min_number = 1

def print_numbers():
     max_number = 9
     min_number = 1
     while True:
         number = random.randint(1,9)
         print number
         time.sleep(1)
         #if number == max_number:
         #    break
         #elif number == min_number:
         #    break

print_numbers()

while print_numbers() == True:
    if print_numbers() == max_number:
        break
    elif print_numbers() == min_number:
        break
