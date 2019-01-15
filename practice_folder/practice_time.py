import time
import random

max_time = input("Please supply a maximum amount of time: ")
start_time = time.time()

print("Sleeping for Thirty seconds.")
time.sleep(30)

while (time.time() - start_time) < float(max_time):
		result = []
		results = random.randint(1,9)
		result.append(results)
		print("Data collected: {}".format(results))
		time.sleep(1)

print(results)

exect_time = time.time() - start_time
print("Finsihed")
print("It took {} seconds ".format(exect_time))
