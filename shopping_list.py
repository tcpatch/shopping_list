import recipe
import os

class ShoppingList:
    def __init__(self):
        self.monday = None
        self.tuesday = None
        self.wednesday = None
        self.thursday = None
        self.friday = None
        self.saturday = None
        self.sunday = None
        self.requested_recipes = None
        self.recipe_book = self.gather_all_recipes()
        self.tag_table = dict()

    def compile_recipes(self):
        self.requested_recipes = [self.monday, self.tuesday, self.wednesday, self.thursday, self.friday, self.saturday, self.sunday]

    @staticmethod
    def gather_all_recipes():
        recipe_book = list()
        for root, dirs, files in os.walk('all_recipes'):
            for fp in files:
                current_recipe = os.path.join('all_recipes', fp)
                recipe_book.append(recipe.Recipe(fp=current_recipe))
        return recipe_book

    def generate_tag_table(self):
        for r in self.recipe_book:
            recipe_tags = r.tag_dict #todo finish...
