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
        self.tags = None

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
            with open(fp, 'r') as f:
                lines = f.readlines()
            #TODO change to all html like tags and parse that way so it isnt hard coded
            self.name = lines[0].strip()
            self.prep_time = lines[1]
            self.cook_time = lines[2]
            self.total_time = self.prep_time + self.total_time
#TODO parse file
#TODO make a function to parse text between html tags and return that

        def parse_tags(self):
            tag_dict = dict()
            for t in self.tags:
                tag_path = t.split('/')
                path_length = len(tag_path)
                current_dict = tag_dict
                for i in range(0, path_length):
                    t = tag_path[i]
                    if t not in current_dict:
                        if i + 1 == path_length:
                            current_dict[t] = tag_path[i+1]
                            break
                        else:
                            current_dict[t] = dict() #todo finish up logic
                            current_dict = current_dict[t]
                    else:
                        current_dict = current_dict[t] #TODO deal with if end of another tag in dictionary...

