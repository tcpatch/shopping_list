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

    def compile_recipes(self):
        self.requested_recipes = [self.monday, self.tuesday, self.wednesday, self.thursday, self.friday, self.saturday, self.sunday]

    def gather_all_recipes(self):
        return None
