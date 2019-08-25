#this one is like your scripts with argv

def print_two(*argv):
	argv1, argv2 = argv
	print("argv1: %s, argv2: %s" % (argv1, argv2))


def print_two_again(argv1, argv2):
	print("argv1: %s, argv2: %s" % (argv1, argv2))


def print_one(argv1):
	print("argv1: %s" % (argv1))

def print_none():
	print("I got nothing")


print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()