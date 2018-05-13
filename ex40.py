# -*- coding: utf-8 -*-

class Song(object): #创建一个类，是从object继承下来的
	
	# 创建实例，把一些我们认为必须绑定的属性强制填写进去
	def __init__(self, lyrics): # 注意init两端各有2各下划线！
		self.lyrics = lyrics #初始化

	def sing_me_a_song(self):
		for line in self.lyrics: # 逐行遍历
			print line
# 可以将以上创建的类封装，以后给出实例时直接拿来用。

happy_day = Song(["Happy birthday to you", # 列表。实例
				  "I don't want to get sued",
				  "So I'll stop right there"])

bulls_on_a_parade = Song(["They rally around the family", # 列表。实例
						  "With pockets full of shells"])

happy_day.sing_me_a_song() # 调用

bulls_on_a_parade.sing_me_a_song() # 调用


