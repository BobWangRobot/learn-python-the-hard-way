#  Here's some new strange stuff, remember type it exactly.

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

# 为什么使用%r时\n换行就不灵了？
# %r就是这个样子，它打印出的是你写出来的方式（或近似方式）。它是用来调试的“原始”格式。

print "Here are the days: ", days
print "Here are the months: ", months

print """ 
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
""" # 三个引号之间不能有空格