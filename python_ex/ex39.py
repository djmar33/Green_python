#################
# 习题39:可爱的字典
#################
# 前言
#
# 区别列表和字典：
# 1.列表：['apple', 'orange'],只可以用数字来索引元素
# 2.字典：{'name': xue, 'age': 22}，不仅可以通过数字索引，还可以通过字符串索引,
#   可以把字典当做“查询表”
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
    }

cities = {
    'CA':'San Francisco',
    'MI':'Detroit',
    'FL':'Jacksonville'
    }

print("-" * 10)

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

#print Detroit
print("Michigan\'s abbreviation is: ", cities[states['Michigan']])
#print Jacksonville
print("Florida has: ", cities[states['Florida']])

print("-" * 10)
#循环遍历states字典，让state,abbrev赋值字典所有key,value参数；
for state, abbrev in states.items():
    print("%s is abbreviated %s" % (state, abbrev))

print("-" * 10)
#循环遍历cities字典，让abbrev,city赋值字典所有key,value参数；
for abbrev, city in cities.items():
    print("%s has the city %s" % (abbrev, city))


print("-" * 10)
#.get语法判断states是否包含texas值，如果没有将返回None；
state = states.get('Texas', None)

if not state:
    print("Sorry,no Texas")
    
#.get语法判断cities是否包含TX值，如果没有将返回None；
city = cities.get('TX', 'Does Not Exist')
print("The city for the state 'TX' is %s" % city)
