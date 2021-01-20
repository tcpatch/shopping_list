import recipe
import os
from collections import Counter
import re
from settings import user_staples, user_exclude_list

class ShoppingList:
    def __init__(self):
        self.monday = None
        self.tuesday = None
        self.wednesday = None
        self.thursday = None
        self.friday = None
        self.saturday = None
        self.sunday = None
        self.requested_recipes = list()
        self.recipe_book = None
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
    
    def show_options(self, selected_tag, tag_level):
        
        all_tags = list()
        ret_dict = dict()

        for r in self.recipe_book:
            for i in r.tags:
                if tag_level > 0:
                    previous_tag = i.split('/')[tag_level - 1]
                else:
                    previous_tag = None
                if previous_tag == selected_tag:
                    current_tag = i.split('/')[tag_level]
                    all_tags.append(current_tag)
                    if i in ret_dict:
                        ret_dict[current_tag].append(r)
                    else:
                        ret_dict[current_tag] = [r]
        all_tags.sort()
        if len(ret_dict.keys()) == 1:
            potential_recipes = ret_dict[list(ret_dict.keys())[0]]
            if len(potential_recipes) == 1:
                potential_recipe = potential_recipes[0]
                for i in potential_recipe.tags:
                    if tag_level > 0:
                        previous_tag = i.split('/')[tag_level - 1]
                    else:
                        previous_tag = None
                    if previous_tag == selected_tag:
                        if i.split('/')[tag_level] == potential_recipe.name and tag_level == len(potential_recipe.tags) - 1:
                            return potential_recipe

        counter = 1
        other_ret_dict = dict()
        for t in set(all_tags):
            print('{})'.format(counter), t)
            other_ret_dict[counter] = t
            counter += 1

       
        return ret_dict, other_ret_dict

    def generate_shopping_list(self):
        needed_ingredients = list()
        for dinner in self.requested_recipes:
            if dinner:
                needed_ingredients.extend([i.split(',')[0] for i in dinner.ingredients])

        for i in user_staples:
            print('{} {}'.format(i[0], i[1]))
        for k, v in Counter(needed_ingredients).items():
            if k not in user_exclude_list:
                print(k, v)
