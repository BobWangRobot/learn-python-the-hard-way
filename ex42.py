# -*- coding: utf-8 -*-

## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object): #创建“Animal”父类
	pass

## is-a
class Dog(Animal): # 创建“Dog”子类（继承自“Animal”父类）

	def __init__(self, name): # 在Dog子类下创建的空对象
		## has-a
		self.name = name # 初始化

## is-a
class Cat(Animal): # 创建“Cat”子类（继承自“Animail”父类）

	def __init__(self, name): # 在Cat子类下创建的空对象
		## has-a
		self.name = name # 初始化

## is-a
class Person(object): # 创建“Person”父类

	def __init__(self, name): # 在”Person“父类下创建一个空对象
		## has-a
		self.name = name # 初始化

		## Person has-a pet of some kind
		self.pet = None # 确保类的self.pet的初始属性被设置为None。

## is-a
class Employee(Person): # 创建“Emyloyee”子类（继承自”Person“父类）

	def __init__(self, name, salary): # 在“Employee”子类下创建一个空对象
		## has-a hmm what is this strange magic?
		super(Employee, self).__init__(name) 
		# super()是用来解决多重继承问题的。
		# 可以可靠的将"Employee"父类的__init__方法运行起来。
		
		## has-a
		self.salary = salary

## is-a
class Fish(object): # 创建“Fish”父类
	pass

## is-a
class Salmon(Fish): # 创建“Salmon”子类（继承自“Fish”父类）
	pass

## is-a
class Halibut(Fish): # 创建“Halibut”子类（继承自“Fish”父类）
	pass

## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## mary has-a pet named satan
mary.pet = satan

## frank has-a salary 120000
frank = Employee("Frank", 120000)

## frank has-a pet named rover
frank.pet = rover

## flipper is-a Fish
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## harry is-a Halibut
harry = Halibut()

