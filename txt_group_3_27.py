###Cooking with Python##

import re, sys, glob, math
from collections import Counter
word_pattern = re.compile("\w[\w\-\']*\w|\w")

###Tokenizing & Organizing###
store = Counter()
tcounts = {}
num2name = []
x = 0
for filename in glob.glob("*.txt"):
	counter = Counter()
	tcounts[x] = counter
	with open(filename) as file:
		for line in file:
			line = line.rstrip()
			line = line.lower()
			tokens = word_pattern.findall(line)
			counter.update(tokens)
	tcounts[x] += counter
	store += counter
	num2name.append((x, filename))
	x += 1

num2name = sorted(num2name, key = lambda x: x[0])

###Searching Dictionaries###
vocabulary = dict(store)
vocabulary['butter']
vocabulary['eggs']
vocabulary['kale']
vocabulary['whisk']
tcounts[0]['butter']
tcounts[0]['butter']/vocabulary['butter']

###Answering Questions###
where_the_kale_at = []
for i in range(10):
	if tcounts[i]['kale'] > 0:
		where_the_kale_at.append(i)

names = []
for i in where_the_kale_at:
	names.append(num2name[i][1])

###String Matching###

temp = open(names[0],'r').read().split('\n')
temp1 = open(names[1],'r').read().split('\n')
doc = [line.lower() for line in temp if line.strip() != '']
doc1 = [line.lower() for line in temp1 if line.strip() != '']

kale = re.compile('kale')

for line in doc:
	if kale.findall(line):
		print(line)

for line in doc1:
	if kale.findall(line):
		print(line)

for i in range(len(doc)):
	if kale.findall(doc[i]):
		print(doc[i - 2], doc[i -1], doc[i], doc[i +1], doc[i+2])

for i in range(len(doc1)):
	if kale.findall(doc1[i]):
		print(doc1[i - 2], doc1[i -1], doc1[i], doc1[i +1], doc1[i+2])

### A Brainy Challenge ###
###Question: What's the most popular way to prepare brains?###

vocabulary['brains']
where_the_brains_at = []
for i in range(10):
	if tcounts[i]['brains'] > 0:
		where_the_brains_at.append(i)

names1 = []
for i in where_the_brains_at:
	names1.append(num2name[i][1])

brainlines = []
brains = re.compile('brains')
for i in names1:
	with open(i) as file:
		for line in file:
			line = line.rstrip()
			line = line.lower()
			tokens = word_pattern.findall(line)
			for y, t in zip(tokens, range(len(tokens))):
				if 'brains' in y:
					brainlines.append((i, tokens[t-4:t+4], t))

meal_options = []
for x in range(len(brainlines)):
	for i,q in zip(brainlines[x][1], range(len(brainlines[x][1]))):
		if i == 'brains':
			meal = (brainlines[x][1][q -1] + ' ' + brainlines[x][1][q])
			if 'the' in meal:
				pass
			elif 'and' in meal:
				pass
			else:
				meal_options.append(meal)	

Popular_meals = {}
for item in meal_options:
    Popular_meals[item] = Popular_meals.get(item, 0) + 1

winner = max(Popular_meals, key=Popular_meals.get)
print(winner)


