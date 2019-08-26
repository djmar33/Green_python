ten_things = "Apples Oranges Crows Telephone Light Sugar"
#修复没有10个东西的列表
print("Wait there\'s not 10 things in that list,let\'s fix that.")
#使用split()函数，将ten_things分割成字符串数组，并赋值给stuff；
stuff = ten_things.split(' ')

more_stuff = ["Day","Night","Song","Frisbee","Corn","Banana","Girl","Boy"]
#进入while循环，stuff长度不等于10，就进入循环，如果大于10将退出循环；
while len(stuff) != 10:
	#使用pop()函数，删除more_stuff列表中最后一个元素。括号里没有参数表示最后一位；
    next_one = more_stuff.pop()
    print("Adding: ",next_one)
    #stuff添加移除的元素，列表总长度+1；
    stuff.append(next_one)
    print("There\'s %d items now." % len(stuff))

print("There we go: ",stuff)

print("Let\'s do some things with stuff.")

#输出stuff第二个元素，因为索引是从0开始，1表示第二个元素；
print(stuff[1])
#输出stuff最后一个元素；
print(stuff[-1])
#删除最后一个元素；
print(stuff.pop())
#列表每个元素中间增加‘ ’空格；
print(' '.join(stuff))
#在stuff列表3-5（不包含5，需要减1），所以是3-4元素之间增加#符号；
print('#'.join(stuff[3:5]))

