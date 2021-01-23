import shopping_list as sl
import recipe


def get_recipe_input(day, shopping_list):
    print('-'*100)
    print('Dinner for {}:'.format(day))
    #TODO add show_options() to shopping_list.py

    selecting = True
    selected_tag = None
    tag_level = 0

    while selecting:
        options, number_mapping = shopping_list.show_options(selected_tag, tag_level)
        response = str(input('Dinner name or tag selection: '))
        try:
            selected_int = int(response)
            if selected_int == 0:
                get_recipe_input(day, shopping_list)
            selected_tag = number_mapping[selected_int]
        except ValueError:
            selected_tag = response.lower()
        if len(options[selected_tag]) == 1 and options[selected_tag][0].name == selected_tag:
            selection = options[selected_tag][0]
            selecting = False
        elif isinstance(options, recipe.Recipe):
            selection = options
            selecting = False
        elif len(options[selected_tag]) == 0:
            print('Uh oh... no recipes left. Starting over')
            get_recipe_input()
        tag_level+=1

    setattr(shopping_list, day, selection)


if __name__ == '__main__':
    # TODO:
    # stuffed zucchini
    # regular pasta
    # kale salad
    # lentils
    # lentils with hot dogs
    # southwest salad
    # beef stew
    # chicken fajita pasta
    # arepas
    # sphagetti squash
    # baked ziti with sausage
    # pulled pork sliders
    # hamburgers
    # kebabas
    # turkey soup
    shopping_list = sl.ShoppingList()
    week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    for day in week:
        get_recipe_input(day, shopping_list)
#        recipe = str(input('Dinner for {}: '.format(day)))
#        setattr(shopping_list, day, recipe)
    shopping_list.compile_recipes()
    shopping_list.generate_shopping_list()

