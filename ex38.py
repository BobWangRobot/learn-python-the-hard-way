# -*- coding: utf-8 -*-

ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there's not 10 things in that list, let's fix that."

stuff = ten_things.split(' ') # 将句子以空格为端点方式分割成逐个单词的列表。
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Gril", "Boy"]

while len(stuff) != 10:
	next_one = more_stuff.pop()
	print "Adding: ", next_one
	stuff.append(next_one)
	print "There's %d items now." % len(stuff)

print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[1]
print stuff[-1] # whoa! fancy
print stuff.pop() # 不注明数字，则默认删除最后一个，并打印出来所删除的项
print ' '.join(stuff) # what? cool!
print '#'.join(stuff[3:5]) # super stellar!