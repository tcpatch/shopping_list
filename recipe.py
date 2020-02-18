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

    @staticmethod
    def as_type(i, _type):
        if _type == 'str':
            ret = str(i)
        elif _type == 'int':
            ret = int(i)
        elif _type == 'float':
            ret = float(i)
        elif _type == 'bool':
            ret = bool(i)
        elif _type == 'long':
            ret = long(i)
        else:
            ret = i
        return ret

    def find_tag(self, lines, tag, _type=None):
        start_tag = '<' + tag + '>'
        end_tag = '</' + tag + '>'
        start = lines.index(start_tag) + 1
        end = lines.index(end_tag)
        contents = lines[start:end]
        if len(contents) == 1:
            contents = contents[0]
        if _type:
            contents = self.as_type(contents, _type)
        return contents
        
    def load_from_file(self, fp):
        with open(fp, 'r') as f:
            lines = f.readlines()
        lines = [i.strip() for i in lines]
        tags = [('name', 'str'), 
                ('prep_time', 'int'),
                ('cook_time', 'int'),
                ('cook_temp', 'int'),
                ('ingredients', None),
                ('recipe', None),
                ('tags', None)]
        for t in tags:
            if t[0] == 'ingredients':
                setattr(self, '_ingredients', self.find_tag(lines, t[0], t[1]))
            else:
                setattr(self, t[0], self.find_tag(lines, t[0], t[1]))
        self.total_time = self.prep_time + self.cook_time

    def parse_tags(self):
        tag_dict = dict()
        for tag in self.tags:
            tag_path = tag.split('/')
            path_length = len(tag_path) - 1
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
        print(tag_dict)

