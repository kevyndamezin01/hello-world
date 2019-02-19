from threading import Timer

def timeout():
	print("Time is up")

def timer():
	t = Timer(1 * 30, timeout)
	t.start()
	while t == True:
		print("Hello")

timer()