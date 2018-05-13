def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes_of_crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket. \n"


print "We can just give the function numbers directly:"
cheese_and_crackers(20,30)


print "OR, we can just use variables from out script:"
amount_of_cheese = 10 #这些值，当它们被传递到函数中以后，函数会为这些变量创建一些临时的版本，当函数运行结束后，这些临时变量就会被废弃了
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese,amount_of_crackers)


print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)


print "And we can combine the two, variables and maths:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 10000)