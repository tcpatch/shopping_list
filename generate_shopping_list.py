class ShoppingList:
    def __init__(self):
        self.monday = None
        self.tuesday = None
        self.wednesday = None
        self.thursday = None
        self.friday = None
        self.saturday = None
        self.sunday = None


if __name__ == '__main__':
    shopping_list = ShoppingList()
    week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    for day in week:
        recipe = str(input('Dinner for {}: '.format(day)))
        setattr(shopping_list, day, recipe)

