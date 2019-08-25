#导入sys的argv模块
from sys import argv
#导入os.path的exists模块；
#exists可以将文件名字符串作为参数，如果文件存在返回True,否则返回False；
from os.path import exists

script, from_file, to_file = argv

print("Copying from %s to %s" % (from_file, to_file))

#we could do these two on one line too, how ?
#打就from_file文件，并且赋值给in_file；
in_file = open(from_file)
#读取in_file文件，并且赋值给indata;
#因为in_file.read()运行一次就会关闭文件；
indata = in_file.read()

#输出indata文件长度：
print("The input file is %d bytes long" % len(indata))

#判断文件是否存在；
print("Does the output file exists? %s" % exists(to_file))

print("Ready, hit RETURN to continue, CTRL-C to abort.")

input()

#打开to_file，并且为读写状态；
out_file = open(to_file, 'w')
#将indata写入out_file里；
out_file.write(indata)

print("Alright, all done.")

#关闭文件；
out_file.close()
in_file.close()

