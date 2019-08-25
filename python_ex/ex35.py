from sys import exit

#金屋子函数
def gold_room():
	print("This room is full of gold. How much do you tack?")

	next = input("> ")
    #判断输入数值包含0，或1，将输入值赋予给how_much变量；
	if "0" in next or "1" in next:
		how_much = int(next)
    #如果不包含0或1的数值，直接退出；
	else:
		dead("Man, learn to type a number.")

    #继续判断包含0或者1变量how_much是否小于50，如果小于50将赢取游戏并退出；
	if how_much < 50:
		print("Nice,you\'re not greedy, you win!")
		exit(0)
    #如果how_much变量大于50,输出你是贪心鬼！
	else:
		dead("You greedy bastard!")

#熊房间函数
def bear_room():
	print("There is a bear here.")
	print("The bear has a bunch of honey.")
	print("The fat bear is in front of another door.")
	print("How are you going to move the bear?")
	bear_moved = False

    #进入循环：
	while True:
		next = input("> ")
        #判断输入变量next是否等于take honey，如果是输出以下信息并返回循环；
		if next == "take honey":
			dead("The bear looks at your then slaps your face off.")
        #否则判断next等于taunt bear ；
        #and not bear_moved 意思就是not False = True；
        #next等于taunt bear and true，将输出以下信息，并将true赋值给bear_moved；然后返回循环；
		elif next == "taunt bear" and not bear_moved:
			print("The bear has moved from the door.You can go through it now.")
			bear_moved = True
        #否则再判断next等于baunt bear and False，该条件为False 才会输出下面信息;
		elif next == "taunt bear" and bear_moved:
			dead("The bear gets pissed off and chews your leg off.")
		#否则再判断next等于open door and bear_moved（True），将进入金屋函数；
		#如果bear_moved为False，该条件将不成立；
		elif next == "open door" and bear_moved:
			gold_room()
		#输入信息没有判断字段，将输出以下信息；
		else:
			print("I got no idea what that means.")

#黑屋函数
def cthulhu_room():
	print("Here you see the great evil Cthulhu.")
	print("He,it,whatever stares at you and you go insane.")
	print("Do you flee for your life or eat your head?")

	next = input("> ")
    #判断flee 在next变量，如果是则进入start（）函数；
	if "flee" in next:
		start()
	#否则判断head 在next变量，如果是则输出以下信息；
	elif "head" in next:
		dead("Well that was tasty!")
	#都不是，则返回黑屋函数；
	else:
		cthulhu_room()
#Good job合成函数；
def dead(why):
	print(why,"Good job!")
	exit(0)
#开始函数；
def start():
	print("You are in a dark room.")
	print("There is a door to your right and left.")
	print("Which one do you take?")

	next = input("> ")
    #判断next为left时，则进入熊房；
	if next == "left":
		bear_room()
	#否则在判断next是否等于right，如果是则进入黑屋；
	elif next == "right":
		cthulhu_room()
	#都不是则输出dead函数；
	else:
		dead("You stuble around the room until you starve.")
#开始函数；
start()
