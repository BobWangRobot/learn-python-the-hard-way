# -*- coding: utf-8 -*-

# create a mapping of state to abbreviation
states = {
	'Oregon': 'OR',
	'Florida': 'FL',
	'California': 'CA',
	'New York': 'NY',
	'Michigan': 'MI'
}

# create a basic set of states and some cities in them
cities = {
	'CA': 'San Francisco',
	'MI': 'Detroit',
	'FL': 'Jacksonville'
}

#add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

#print out some cities
print '-' * 10
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']

# print some states
print '-' * 10
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']

# do it by using the states then cities dict
print '-' * 10
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states["Florida"]]

# print every state abbreviation
print '-' * 10
for state, abbrev in states.items(): # dict.items() 返回可遍历的（键，值）元组数组。
	print "%s is abbreviated %s" % (state, abbrev)

# print every city in state
for abbrev, city in cities.items():
	print "%s has the city %s" % (abbrev, city)

# now do both at the same time
print '-' * 10
for state, abbrev in states.items():
	print "%s state is abbreviated %s and has city %s" % (state, abbrev, cities[abbrev])

print '-' * 19
# safely get a abbreviation by state that might not be there
state = states.get('Texas', None) 
# dict.get(key.default = None) 
# key 字典中要查找的键
# default 如果指定键的值不存在时，返回该默认值

# 返回指定值的键，如果值不在字典中返回默认值None

if not state:
	print "Sorry no Texas."

# get a city with a default value
city = cities.get('TX', 'Dose Not Exist')
print "The city for the state 'TX' is: %s" % city


