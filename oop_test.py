# -*- coding: utf-8 -*-

# 这个程序的作用是在网一个网址获取一些单词，用这些单词命名程序的代码块和其中的元素。
# 不管你在>后输入什么，程序都会将该代码块的含义及作用打印出来。
# 当你按Ctrl+Z的时候，程序退出并打印Bye

import random # 导入一个产生随机数的库
from urllib import urlopen # 从urllib库中引入urlopen函数
# Python urllib库提供了一个从指定的URL地址获取网页数据，然后对其进行分析处理，获取想要的数据。
# urllib()函数，创建一个类文件对象为指定的url来读取。
# 详细点就是，创建一个表示远程url的类文件对象，然后像本地文件一样操作这个类文件对象来获取远程数据。
# 参数url表示远程数据的路径，一般是网址；参数data表示以post方式提交到url的数据
#(玩过web的人应该知道提交数据的两种方式：post与get。如果你不清楚，也不必太在意，一般情况下很少用到这个参数)；
# 参数proxies用于设置代理（这里不详细讲怎么使用代理，感兴趣的看客可以去翻阅Python手册urllib模块）。
# urlopen返回 一个类文件对象，他提供了如下方法：
	# 1. 参数 url 表示远程数据的路径，一般是 http 或者 ftp 路径。
	# 2. 参数 data 表示以 get 或者 post 方式提交到 url 的数据。
	# 3. 参数 proxies 表示用于代理的设置。

import sys # 引入sys库

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = [] # 列表

PHRASES = {
	"class %%%(%%%):":
	 "Make a class named %%% that is-a %%%.",
	"class %%%(object):\n\tdef __init__(self, ***)" :
	 "class %%% has-a __init__ that takes self and *** parameters.",
	"class %%%(object):\n\tdef ***(self, @@@)":
	   "class %%% has-a function named *** that takes self and @@@ parameters.",
	"*** = %%%()":
	  "Set *** to an instance of class %%%.",
	"***.***(@@@)":
	  "From *** get the *** function, and call it with parameters self, @@@.",
	"***.*** =  '***'":
	  "From *** get the *** attribute and set it to '***'." 
}

# do they want to drill phrases first
PHRASE_FIRST = False
if len(sys.argv) == 2 and sys.argv[1] == "english":
	PHRASE_FIRST = True

# load up the words from the website
for word in urlopen(WORD_URL).readline(): # 逐行遍历
	WORDS.append(word.strip())


def convert(snippet, phrase):
	class_names = [w.capitalize() for w in
				   random.sample(WORDS, snippet.count("%%%"))]
	other_names = random.sample(WORDS, snippet.count("***"))
	results = []
	param_names = []

	for i in range(0, snippet.count("@@@")):
		param_count = random.randint(1, 3)
		param_names.append(', '.join(random.sample(WORDS, param_count)))

	for sentence in snippet, phrase:
		result = sentence[:]

		# fake class param_names
		for word in class_names:
			result = result.replace("%%%", word, 1)

		# fake other names
		for word in other_names:
			result = result.replace("***", word, 1)

		# fake parameter lists
		for word in param_names:
			result = result.replace("***", word, 1)

		results.append(result)

	return results

# keep going until they hit CTRL-D
try:
	while True:
		snippets = PHRASES.keys()
		random.shuffle(snippets)

		for snippet in snippets:
			phrase = PHRASES[snippet]
			question, answer = convert(snippet, phrase)
			if PHRASE_FIRST:
				question, answer = answer, question

			print question

			raw_input("> ")
			print "ANSWER:  %s\n\n" % answer
except EOFError:
	print "\nBye"

