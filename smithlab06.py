# AP CSP 2018 - 2019 ~ Mrs. Vollucci
# Lab 06: Higher-Order Functions

from functools import reduce

# Example 1: iterate instead of map
items = [1, 2, 3, 4, 5]
squared_iter = []
for i in items:
    squared_iter.append(i**2)

# Example 2: map
squared = list(map(lambda x: x**2, items))
#print(squared)

# Example 3: reduce
product = reduce((lambda x,y: x*y), items)

# Exercise 1: Use filter to keep nums divisible by 3
nums = [2, 3, 4, 5, 6, 7, 8 , 9]
divisibleby3 = list(filter((lambda x: x % 3 == 0), nums))
#print(divisibleby3)
# Fill in one line of code here
# Fill in print statement with result here

# Exercise 2: All true?
bools = [True, False, True, False, False]
true = reduce((lambda x, y: x and y), bools)
#print(true)
# Fill in one line of code here
# Fill in print statement with result here

# Exercise 3: Opposite Value Iterative
def opp_val_iter (x):
	y = []
	for i in x:
		y.append(not i)
	return y
#print(opp_val_iter(bools))
# Fill in code here for function
# Fill in print statement with result here
  
# Exercise 4: Opposite Value HOF
opposite = list(map((lambda x: not x),bools))
# Fill in one line of code here
# Fill in print statement with result here

# Exercise 5: How many true?
H_m_t = list(filter((lambda x: x == True), bools))
#print(len(H_m_t))
# Fill in one line of code here
# Fill in print statement with result here

# Exercise 6: Create Iterative Filter
def filter_iter (fn, values):
	y = []
	for v in values:
		if(fn(v) == True):
			y.append(v)
	return y
#
# Fill in code here for function
  
# Exercise 7: Test Your Iterative Filter
nums = [0, -1, 1, -2, 2, 3, -3]
print(' 7:', filter_iter(lambda x: x >= 0,nums))
# Fill in expression here which uses your iterative filter
# Fill in print statement with result here
# result: [0, 1, 2, 3]

# Exercise 8: Sum of Cubes of Odds in List
nums = [1, 2, 3, 4, 5]
def oddsum (x):
	y = 0
	for i in x :
		if (i % 2 == 1):
			y += pow(i, 3)
	return y
print(' 8:', oddsum(nums))
# Fill in code here for function

# Exercise 9: HOFs Implementation of Sum of Cubes of Odds
nums = [5, 4, 3, 2, 1]
sumodd = reduce(lambda sum, x: sum + pow(x, 3), filter(lambda x: x % 2 == 1, nums), 0)
# Fill in one line of code here
# Fill in print statement with result here
print(' 9:', sumodd)

# Exercise 10: Make Acronym
phrase = "Saint Francis High School is the best"
# Fill in one line of code here


acronym = reduce(lambda ac, word: ac + word[0], filter(lambda x: x[0].isupper(), phrase.split()), '')
# Fill in print statement with result here
print('10:', acronym)