i = 0
numbers = []

while i < 6:
	print "At the top i is %d" % i
	numbers.append(i)
    
	i = i + 1 # 一定要写递增条件，不然就会一直循环0，陷入死循环。
# 	print "Numbers now: ", numbers
# 	print "At the bottom i is %d" % i


# print "The numbers: "

# for num in numbers:
#  	print num