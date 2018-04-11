"""You have experienced a devestating personal trauma and want to eat indulgently to accompany a night in bed with a sad French New Wave 
Film and fuel a long distance, contemplative run in the morning. Your problem is the following: you want the most bang for your caloric 
buck and refuse to go to Wegmans and walk through the produce section - that once vibrant cosmos full of glimmers of vegetal, nourishing meals
together - on your way to the dairy. You are, in many ways, stuck alone with what you've got. Using Python, find out how which combination of 
cookies and brownies will best utilize your panty and slow your broken heart. Then, find out how many miles you will need to run at an 8:24
pace to undo your decadence"""

###Recipes and stock###

Brownies = ['two sticks of butter', 'two tablespoons of vegetable oil', 'one cup of sugar', 'one cup of brown sugar', 'four large eggs', 
'one tablespoon of vanilla extract', 'one teaspoon of salt', 'one cup of flour', 'seven ounces of chocolate']

Cookies = ['three-fourth cup of sugar', 'three-fourth cup of brown sugar', 'two sticks of butter', 'one teaspoon of vanilla extract',
 'one egg', 'two cups of flour', 'one teaspoon of baking soda', 'one teaspoon salt', 'twelve ounces of chocolate']

Pantry = ['six sticks of butter', 'thirty-two tablespoons of vegetable oil', 'five cups of sugar', 
'three cups of brown sugar', 'twelve large eggs', 'five tablespoons of vanilla extract', 'sixty teaspoons of salt', 
'five cups of flour', 'twenty-four ounces of chocolate', 'twelve teaspoons of baking soda']

###Nutritional info###

Brownies_per_recipe = 16

Calories_per_brownie = 160

Cookies_per_recipe = 48

Calories_per_cookie = 78

Calories_burned_per_mile = 147

"""Problem one: The first issue we have is that we're going to need to turn the lists of texts into integers that
 we can perform mathematic operations with. As for the data structure we want, tuples would be the natural choice. 
 The function of the code below is to take 'two sticks of butter' and turn it into the following tuple (2, sticks, butter). 
 We will make code here that will then become a defition we can use in problem two"""

Brownies_as_data = []

"""What items will we need to add to this list for it to work with larger numbers? What other limitations does this strategy pose?"""
Word_to_number = [('one', 1), ('two', 2), ('three', 3), ('four', 4), ('five', 5), ('six', 6), ('seven', 7), 
('eight', 8), ('nine', 9), ('ten', 10)]

tokenizer = re.compile("\w[\w\-\']*\w|\w")

for ingredient in Brownies:
	x = tokenizer.findall(ingredient)
	for i in Word_to_number:
### 1.)Finish this if statment###
		if :
			digit_value = i[1]
	for t in range(len(x)):
### why do we need both of these if statements? ###
		if 'of' in x:
			if x[t] == 'of':
				ingredient = " ".join(x[t+1: ])
				measurement = x[t-1]
		else:
			ingredient = x[-1]
			measurement = x[-2]	
###2.)Write a piece of code that will add a tuple containing the digit_value, ingredient, and measurement to Brownies_as_data###


"""Problem two: Brownies was the easy list, but now you need to build code that can handle numerical representations of words over 
ten and partial measurements"""
def word_to_number(str):
	oneteens = [('one', 1), ('two', 2), ('three', 3), ('four', 4), ('five', 5), ('six', 6), ('seven', 7), ('eight', 8), ('nine', 9), 
	('ten', 10), ('eleven', 11), ('twelve', 12), ('thirteen', 13), ('fourteen', 14), ('fifteen', 15), ('sixteen', 16), ('seventeen', 17),
	 ('eighteen', 18), ('nineteen', 19)]
	tens = [('twenty', 20), ('thirty', 30), ('forty', 40), ('fifty', 50), ('sixty', 60), ('seventy', 70), ('eighty', 80), ('ninety', 90)]
	if len(str) > 1:
		if '-' in str:
			x = str.split('-')
			for numbers in tens:
				if numbers[0] in x[0]:
					ten = numbers[1]
			for numbers in oneteens:
				if numbers[0] in x[1]:
					one = numbers[1]
			return(ten + one)
		elif len(str):
			for numbers in oneteens:
				if numbers[0] in str:
					one = numbers[1]
			return(one)
	else:
		pass
"""3.)Define a function called 'ither' that will take words that end in a 'th' and return the word without a th (fourth get four, worth gets wor)"""



"""4.)Turn the code below into a definition called 'fraction_to_decimal' that will accept a list"""
for ingredient in Cookies:
	x = tokenizer.findall(ingredient)
	for i in x:	
		if '-' in i:
			q = i.partition('-')
			t = word_to_number(ither(q[0])) / word_to_number(ither(q[2]))
			print(t)

"""Problem three: write a comprehensive definition that will turn Brownies, Cookies, and Pantry into itemized lists of tuples. Not that you do not
need to redfine word_to_number, ither, or fraction_to_decimal"""

Brownie_as_data = []
Cookie_as_data = []
Pantry_as_data = []
def itemizer(list):



Brownies_as_data = itemizer(Brownies)
Cookies_as_data = itemizer(Cookies)
Pantry_as_data = itemizer(Pantry)





