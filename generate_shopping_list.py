import shopping_list as sl


def get_recipe_input(day, shopping_list):
    print('Dinner for day {}'.format(day))
    #TODO add show_options() to shopping_list.py
    options = shopping_list.show_options()
    response = str(input('Dinner name or tag selection: '))
    if response.isdigit():
        response = options[response]
    #TODO add parse_selection() to shopping_list.py
    selection = shopping_list.parse_selection(response)
    if selection == 'continue':
        get_recipe_input(day, shopping_list)
    else:
        setattr(shopping_list, day, selection)


if __name__ == '__main__':
    shopping_list = sl. ShoppingList()
    week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    for day in week:
        get_recipe_input(day, shopping_list)
#        recipe = str(input('Dinner for {}: '.format(day)))
#        setattr(shopping_list, day, recipe)
    shopping_list.compile_recipes()
    print(shopping_list.requested_recipes)

