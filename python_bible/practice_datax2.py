import time
import random

def print_numbers():
     max_number = 15
     min_number = 4
     while True:
         number = random.randint(1,20)
         print number
         time.sleep(1)
         if number >= max_number:
             break
         elif number <= min_number:
             break

print_numbers()


