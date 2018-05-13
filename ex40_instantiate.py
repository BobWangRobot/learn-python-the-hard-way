# -*- coding: utf-8 -*-

class MyStuff(object):

	def __init__(self):
		self.tangerine = "And now a thousand years between"

	def apple(self):
		print "I AM CLASSY APPLES!"

# 类： 通过类，你可以把一组函数和数据放大一个容器当中，从而用“ . ” 操作符访问它们。

thing = MyStuff() # 将thing指向创建的类
thing.apple() # 访问类里面的函数
print thing.tangerine # 访问类里面的变量