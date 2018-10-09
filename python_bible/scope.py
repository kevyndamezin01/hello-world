# Global Scope variable
a = 250

def f1():
	# Local variable using the global variable.
	b = a + 10
	print(b)

def f2():
	# Local Scope variable
	a = 50
	print(a)

f1()
f2()
print(a)

# if a variable is inside a function then it is a local scope and can,
# not be called on through any other function, a variable that is ,
# outsdie of a function is classed as a global scope and can be used,
# in any function.

# The local scope function will take priority over a global scope function.

# You are able to overwrite a global variable inside a function.
# You do this by using the function global inside the function. 

a = 250

def f3():
	# By calling global here it allows use to change the value of the,
	# global scope function a 
	global a # Global
	a = 100
	print(a)

def f4():
   a = 50 # Local
   print(a)

f3()
f4()
print(a)

# You can use list and dictionaries with this, and change values,
# in the list using the slicing method.
a = [1,2,3]

def f5():
	a[0] = 5
	print(a)

print(a)
f5()

