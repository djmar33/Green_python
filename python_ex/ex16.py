#导入sys里的argv模块
from sys import argv

script, filename = argv

print("We're going to erase %s ." % (filename))

print("If you don't want that,hit CTRL-C (^C).")

print("If you do want that,hit RETURN.")

input("?")
#打开文档
print("Opening the file..")
target = open(filename,'w')

#清空文档
print("Truncating the file . Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")
#将内容赋值到变量里
line1 = input("line 1:")

line2 = input("line 2:")

line3 = input("line 3:")

print("I'm going to write write these to the file.")
#写入文档里
target.write(line1)
target.write("\n")

target.write(line2)
target.write("\n")

target.write(line3)
target.write("\n")

#关闭文档
print("And finally,we close it.")
target.close()