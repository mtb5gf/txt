
import re

Brownies = ['two sticks of butter', 'two tablespoons of vegetable oil', 'one cup of sugar', 'one cup of brown sugar', 'four large eggs', 
'one tablespoon of vanilla extract', 'one teaspoon of salt', 'one cup of flour', 'seven ounces of chocolate']

Cookies = ['three-fourth cup of sugar', 'three-fourth cup of brown sugar', 'two sticks of butter', 'one teaspoon of vanilla extract',
 'one egg', 'two cups of flour', 'one teaspoon of baking soda', 'one teaspoon salt', 'twelve ounces of chocolate']

Pantry = ['six sticks of butter', 'thirty-two tablespoons of vegetable oil', 'five cups of sugar', 
'three cups of brown sugar', 'twelve large eggs', 'five tablespoons of vanilla extract', 'sixty teaspoons of salt', 
'five cups of flour', 'twenty-four ounces of chocolate', 'twelve teaspoons of baking soda']

Brownie_Recipe = ['Preheat oven to 325°F. Line an 8x8x2" glass baking dish with foil, pressing firmly into pan and leaving a 2" overhang. Coat foil with nonstick spray; set baking dish aside.', 'Melt butter in a small saucepan over medium heat. Let cool slightly. Whisk sugar, cocoa, and salt in a medium bowl to combine. Pour butter in a steady stream into dry ingredients, whisking constantly to blend. Whisk in vanilla. Add eggs one at a time, beating vigorously to blend after each addition. Add flour and stir until just combined (do not overmix). Scrape batter into prepared pan; smooth top.',
'Bake until top begins to crack and a toothpick inserted into the center comes out with a few moist crumbs attached, 25-30 minutes.', 'Transfer pan to a wire rack; let cool completely in pan. Using foil overhang, lift brownie out of pan; transfer to a cutting board. Cut into 16 squares.']

Cookie_ Recipe = ['Preheat oven to 350 degrees F (175 degrees C).', 'Cream together the butter, white sugar, and brown sugar until smooth. Beat in the eggs one at a time, then stir in the vanilla. Dissolve baking soda in hot water. Add to batter along with salt. Stir in flour, chocolate chips, and nuts. Drop by large spoonfuls onto ungreased pans.', 'Bake for about 10 minutes in the preheated oven, or until edges are nicely browned.']

Brownies_as_data = []

Word_to_number = [('one', 1), ('two', 2), ('three', 3), ('four', 4), ('five', 5), ('six', 6), ('seven', 7), 
('eight', 8), ('nine', 9), ('ten', 10)]

tokenizer = re.compile("\w[\w\-\']*\w|\w")

for ingredient in Brownies:
	x = tokenizer.findall(ingredient)
	for i in Word_to_number:
		if x[0] == i[0]:
			digit_value = i[1]
	for t in range(len(x)):
		if 'of' in x:
			if x[t] == 'of':
				food = " ".join(x[t+1: ])
				measurement = x[t-1]
		else:
			food = x[-1] 
			measurement = x[-2]	
	Brownies_as_data.append((digit_value, food, measurement)

#Make a function that matches ingredient to place in recipe#
def placer(lst1, lst2):
#Make a function that classifies which food group each ingredient is in#
def food_grouper (lst):
#Make a function that will substitutes non-vegan ingredients### 
def veganizer(lst):
# Make a function that will convert all units to ounces###


