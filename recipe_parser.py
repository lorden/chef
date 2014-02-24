import json

class RecipeParser:
	def __init__(self, filename):
		with open(filename) as json_data:
			self.recipe = json.load(json_data)

	def find_ingredient(self, ingredient_keyword):
		possible_matches = []
		for ingredient in self.recipe['ingredients']:
			if ingredient_keyword in ingredient['ingredient']:
				possible_matches.append(ingredient)
		return possible_matches

	def get_ingredients(self):
		ingredients = []
		for ingredient in self.recipe['ingredients']:
			ingredients.append(ingredient['amount'] + ' ' + ingredient['ingredient'])
		return ingredients

	def get_instruction(self, instruction_number=None):
		if instruction_number is not None:
			return self.recipe['instructions'][instruction_number]
		else:
			return self.recipe['instructions']

icecreamcone = RecipeParser('icecreamcone.json')
print icecreamcone.get_ingredients()
print icecreamcone.find_ingredient('cone')
print icecreamcone.get_instruction(2)