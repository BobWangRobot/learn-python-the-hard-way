# -*- coding: utf-8 -*-

# 在运行前或运行后替换

class Parent(object):

	def altered(self):
		print "PARENT altered()"

class Child(Parent):

	def altered(self):
		print "CHILD, BEFORE PARENT altered()"
		super(Child, self).altered() # 调用父类
		print "CHILD, AFTER PARENT altered()"

dad = Parent()
son = Child()

dad.altered()
son.altered()