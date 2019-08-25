print("Let's practice everyting.")

print('You \'d need to know \' about escapes with \\ that do \n newlines and \t tabs.')

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion form intuition
and requires an explanation
\n\t\t where there is none.
"""

print("--------------")
print(poem)
print("--------------")


five = 10 - 2 + 3 - 6
print("This should be five: %s" % five)

def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans / 1000
	crates = jars / 100
	return jelly_beans, jars, crates

start_point = 10000
#后面把jelly_beans变量又叫beans，这就是函数工作原理；
#函数内部的变量都是临时的；
#当函数返回以后，返回值可以被赋予一个变量；
beans, jars, crates = secret_formula(start_point)

print("With a starting point of : %d" % start_point)
print("We'd have %d beans , %d jars , and %d crates." % (beans, jars, crates))

start_point = start_point / 10

print("We can also do that this way:")
print("We'd have %d beans , %d jars, and %d crates." %secret_formula(start_point))