def break_words(stuff):
	"""This function will break up words for us.""" # 文档注释，可用help(ex25)调用查看
	words = stuff.split() # split()将句中每个单词分割出来，中间加空格
	return words

def sort_words(words):
	"""Sorts the words."""
	return sorted(words) # 按照单词首字母排序

def print_first_word(words):
	"""Prints the first word after poping it off."""
	word = words.pop(0) # 删除第一个单词并打印
	print word

def print_last_word(words):
	"""Prints the last word after poping if off."""
	word = words.pop(-1) # 删除最后一个单词并打印
	print word

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
