# This one is like your scripts with argv
def print_two(*args): # 把函数的所有参数都接收进来，然后放到args的列表中去
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)

# Ok, that *args is actuallu pointless,we can just do this
def print_two_again(arg1,arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)

# This just takes one argument
def print_one(arg1):
	print "arg1: %r" % arg1

# This one takes no argumengs
def print_none():
	print "I got nothin'."


print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()