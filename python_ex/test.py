the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

for number in the_count:
	print("This is count %d" % number)

for fruit in fruits:
	print("I got %s" % fruit)

elements = []

for i in fruits:
	print("Adding %s to the list." % i)
	elements.append(i)

for i in elements:
	print("elements was: %s" % i)