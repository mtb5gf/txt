###small potatoes###

import re

Ingredients_you_have = [(1, "potato", "pound"), (8, "tumeric", "tablespoon"), (16, "sugar", "tablespoon"),
 (8, "garlic", "cloves"), (12, "oil", "tablespoon"), (8, "soy sauce", "tablespoon"), (2, "cumin seed", "teaspoon"), (4, "ginger", 
 "tablespoon"), (1, "cashew", "cup"), (1, "shallot", "large")]

Korean_potatoes = [(3, "soy sauce", "tablespoon"), (.25, "mirin", "cup"), (1, "gochujang", "tablespoon"),
(1, "sugar", "tablespoon"), (2, "garlic", "cloves"), (1, "oil", "tablespoon"), (2, "potato", "pound"),
(2, "sesame oil", "teaspoon"), (2, "rice vinegar", "teaspoon"), (2, "sesame seed", "teaspoon"),
(2, "scallion", "whole")]

Harissa_roasted_potatoes = [(3, "potato", "pound"), (5, "oil", "tablespoon"), (5, "harissa", "tablespoon"), 
(.25, "cilantro", "cup"), (1, "lemon", "whole")]

Ginger_tumeric_potatoes = [(3, "oil", "tablespoon"), (1, "shallot", "large"), (1, "ginger", "tablespoon"),
(2, "black mustard seed", "teaspoon"), (1.5, "cumin seed", "teaspoon"), (.5, "red pepper flake", "teaspoon"),
(.5, "tumeric", "teaspoon"), (.75, "potato", "pound"), (.75, "green bean", "pound"), (1, "lemon", "whole"),
(.5, "grape tomato", "cup"), (.5, "cashew", "cup"), (.5, "cilantro", "cup"), (1, "chile", "whole")]

Servings = [("Korean", 4), ("Middle Eastern", 4), ("Indian", 6) ]

### Name, number of servings they will eat, what they normally bring, food preferenc###
Dining_preferences = [("Bruce", 1.5, "Wine", "Korean"), ("Thadeus", .25, "Fine Cheese which he eats instead of your food",
 "Middle Eastern"), ("Grace", .82, "Blackberries", "Korean"), ("Sherbert F. Tucker", 1.33, "Gelato", "Indian"), 
("Pastor Colonel Mustard, MD.", .4, "Dark Stories from his past, whimsy undergirded by regret", "Indian"), ("Posie Daggershark", 2.1, 
"Hazelnuts and Unfrosted Poptarts", "Middle Eastern"), ("Thurston Thirstquencher", .9, "The beat, guff", "whatever works, I don't even like potatoes")	]


###This function will subtract the ingredients needed in the dish from the ingredients you have on hand###
def What_do_I_need(lst1, lst2):

	### will return a list of tuples containing the quantity of food needed, the food item needed, and the measurement###

###This function will price and sum the amount you would spend on each recipe###
def What_will_it_cost(lst1, lst2):
	###Please refer to the Wegmans website for pricing###
	###will return a float. I.E. 16.74 ###

###This function will tell you how many servings you should make. Note, you will want to double the person's serving size if the meal###
###in question matches their food preference. For instance, when measuring the amount of servings you would need for a Korean dish, you###
####would count Bruce as 3 instead of 1.5 since he likes Korean food. Also, be sure to add your own preferences.###
def How_much_should_I_make(lst1, lst2, lst3):



	### will return the the number of times you'll need to double the recipe to feed yourself. An integer would be best###

### Code we will use###
kp = What_do_I_need(Ingredients_you_have, Korean_potatoes)
hrp =What_do_I_need(Ingredients_you_have, Harissa_roasted_potatoes)
gtp = What_do_I_need(Ingredients_you_have, Ginger_tumeric_potatoes)

quant_kp = How_much_should_I_make(kp, Servings, Dining_preferences)
quant_hrp = How_much_should_I_make(hrp, Servings, Dining_preferences)
quant_gtp = How_much_should_I_make(gtp, Servings, Dining_preferences)

price_kp =  What_will_it_cost(quant_kp, kp)
price_hrp = What_will_it_cost(quant_hrp, hrp)
price_gtp = What_will_it_cost(quant_gtp, gtp)

### Oh wait, you just found out that Thadeus won't be able to make it and instead his identical cousin Chester###
###, who typically eats 3 servings of food, brings whiskey and firecrackers, and has a penchant for Middle Eastern###
### food will be coming. Write code to reflect this change of plans and recalculate your results###


### final bit of code###
print(price_kp, price_hrp, price_gtp)