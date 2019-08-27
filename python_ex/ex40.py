#################
# 习题40:模块、类、对象
#################

#知识点：
#1、python是一种“面向对象编程语言（Object Oriented  Programming Language）”
#2、面向对象编程（简称OOP）
#3、class（类），可以让程序架构更为整齐。
#4、模块和字典差不多，使用方式有点类似，只是语法不同而已。
#  mystuff[`apple`] #字典调取apple
#  mystuff.apple() #模块调取apple
#5、类和模块差不多；
#  模块：可以把模块当做一种特殊的字典，通过他们可以存储一些python代码，可以通过“.”操作符访问这些代码；
#  类：可以把一组函数和数据放到一个容器中，从而用“.”操作符访问这些代码；

class Song(object):
    #python中定义经常会用到__init__函数，双下划线开头的函数声明该属性为私有；不能在类外部被使用和访问。
    #__init__函数支持带参数类的初始化，也可以为声明该类的属性(类中变量)。
    #__init__函数第一个参数必须为self，后续参数为自定义；
    #__init__用法和理解：https://blog.csdn.net/luzhan66/article/details/82822896
    def __init__(self, lyrics):   
        self.lyrics = lyrics
        print(lyrics)

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy birthday to you",
                   "I don\'s want to get sued",
                   "So I\'ll stop right there"])

bulls_on_parade = Song(["They rally around the famil",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()
