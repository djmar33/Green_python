def break_words(stuff):
	"""This function will break up words for us. """
	words = stuff.split(' ')
	return words

#排序操作；
def sort_words(words):
	"""Sorts the words."""
	return sorted(words)
#输出列表第一个字符；
def print_first_word(words):
	"""Prints the first word after popping it off."""
	word = words.pop(0)
	print(word)
#输出列表第最后一个字符；
def print_last_word(words):
	"""Print the last word afert popping it off."""
	word = words.pop(-1)
	print(word)

def sort_sentence(sentence):
	"""Takes in a full sentence and returns the sorted words."""
	words = break_words(sentence)
	return sort_words(words)

def print_first_and_last(sentence):
	"""Prints the first and last words of the sentence."""
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words)

def print_first_and_last_sorted(sentence):
	"""Sorts the words then prints the first and last one."""
	words = sort_sentence(sentence)
	print_first_word(words)
	print_last_word(words)



#导入ex25.py文件
# >>> import ex25
#将句子赋值给sentence变量，后面测试将使用该变量；
# >>> sentence = "All good things come to those who wait."
#调用ex25里的break_words函数；
# >>> words = ex25.break_words(sentence)
# >>> words

#调用ex25.sort_word；
# >>> sorted_words = ex25.sort_words(words)
#查看sorted_words数据
# >>> sorted_words

#调用ex25.print_first_word(words)，将输出第一个字符；
# >>> ex25.print_first_word(words)
# All

# #调用ex25.print_last_word(words)，将输出第最后一个字符；
# >>> ex25.print_last_word(words)
# wait.

# sentence = "All good things come to those who wait."
# words = ex25.break_words(sentence)

# words

# sorted_words = ex25.sort_words(words)

# sorted_words

# ex25.print_first_word(words)

# ex25.print_last_word(words)

# words
# ex25.print_first_word(sorted_words)

# ex25.print_last_word(sorted_words)

# sorted_words

# sorted_words = ex25.sort_sentence(sentence)

# sorted_words
# ex25.print_first_and_last(sentence)
# ex25.print_first_and_last_sorted(sentence)