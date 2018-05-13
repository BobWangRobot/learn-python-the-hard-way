print "How old are you?", # 加结尾的逗号，这样的话print就不会输出换行符而结束这一行跑到下一行去了。
age = raw_input() # 试试x = int(raw_input() ,它会把用户输入的字符串用int() 转换成整数。  

#input()会把你输入的东西当作python代码进行处理，这么做会有安全问题，你应该避开这个函数。

print "How tall are you?",
height = raw_input()
print "How much do you weight?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)
