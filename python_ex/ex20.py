from sys import argv

sciprt, input_file = argv

#定义函数，打开变量f的文件；
def print_all(f):
	print(f.read())

#读取文件行数；
def print_a_line(line_count, f):
	print(line_count, f.readline())


#seek()方法用于移动文件读取指针到指定位置。
def rewind(f):
	f.seek(0)

#打开文件，并且赋值给current_file;
current_file = open(input_file)


print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

print("Let's print three lines:")

rewind(current_file)

current_line = 1

print_a_line(current_line, current_file)

current_line = current_line + 1

print_a_line(current_line, current_file)


current_line = current_line + 1

print_a_line(current_line, current_file)