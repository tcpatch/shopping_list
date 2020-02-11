import all_ingredients

class Recipe:

    def __init__(self, name=None, prep_time=0, cook_time=0, total_time=0, cook_temp=0, ingredients=list(), recipe=None, sub_recipe=None, fp=None):
        self.all_ingredients = all_ingredients.Ingredients() 
        
        self.name = name
        self.prep_time = prep_time
        self.cook_time = cook_time
        if total_time > 0:
            self.total_time = total_time
        else:
            self.total_time = self.prep_time + self.cook_time
        self.cook_temp = cook_temp
        self._ingredients = ingredients
        self.recipe = recipe
        self.sub_recipe = None

        @property
        def ingredients(self):
            return self._ingredients

        @ingredients.setter
        def ingredients(self, ingredients):
            for i in ingredients:
                if i not in self.all_ingredients:
                    self.all_ingredients.add(i)
            self._ingredients = ingredients

        def load_from_file(self, fp):
            pass
