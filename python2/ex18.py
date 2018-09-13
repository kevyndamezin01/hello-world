# This one is like your scripts with args:
# Here we have called for the args command.
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# Ok, that "Args is actually pointless, we can just do this"
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# This just takes one argument
def print_one(arg1):
    print "arg1: %r" % arg1

# This one takes no arguments
def print_none():
    print "I got nothin'."

# By defining what each function is set two, this allows the script to
# Automatically swap out the 'args' for what the value of arg1 is actually
print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()
