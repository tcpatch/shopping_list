import ingredient

class Ingredients:
    def __init__(self, ingredient_list='ingredient_list'):
        self.all_ingredients = list()
        self.ingredient_list = ingredient_list
        self.load_ingredients()

    def load_ingredients(self):
        with open(self.ingredient_list, 'r') as fp:
            lines = fp.readlines()
        for i in lines:
            self.all_ingredients.append(ingredient.Ingredient(i))
    
    def add(self, ingredient, aisle=None, price=None):
        self.all_ingredients.append(ingredient.Ingredient([ingredient, aisle, price]))
        with open(self.ingredient_list, 'a') as fp:
            fp.write(ingredient + ',' + str(aisle) + ',' + str(price) + '\n')

