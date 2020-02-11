import shopping_list as sl

if __name__ == '__main__':
    shopping_list = sl. ShoppingList()
    week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    for day in week:
        recipe = str(input('Dinner for {}: '.format(day)))
        setattr(shopping_list, day, recipe)
    shopping_list.compile_recipes()
    print(shopping_list.requestes_recipes)

