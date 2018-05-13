# -*- coding: utf-8 -*-

x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x 
print y

print "I said: %r." % x # %r用来debug比较好，因为它会显示变量的原始数据（raw data），而%s和其他的符号则是用来像用户显示输出的
print "I also sail: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of ..."
e = "a string with a right side."

print w + e
