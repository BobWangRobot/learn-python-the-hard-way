print "Let's practice everything."
print "You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs."
# \t 横向制表符，输出一个制表符后不换行。

poem = """
\tThe lovely world 
with logic so firmly planted
cannot discern \n the needs of lovely
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print "-------------------"
print poem
print "-------------------"


five = 10 - 2 + 3 - 6
print "this should be five: %s" % five

def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans / 1000
	crates = jars / 100
	return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point)
# 函数内部的变量都是临时的，当你的函数返回以后，返回值可以被赋予一个变量，这里创建了一个新变量 beans ，用来存放函数的返回值。
# 这就是为什么jelly_beans 后面又变成了beans。

print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, %d crates." % (beans, jars, crates)

start_point  /= 10

print "We can also do that this way:"
print "We'd have %d beans, %d jars, %d crates." % secret_formula(start_point)
