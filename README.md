# shopping list

## overview

The purpose of this repository is to generate shopping lists from a list of recipes  ultimately with a user interface made with Flask or Django.

## current state

Bare bone objects are written to hold ingredients and recipes.

* recipe.py object to hold a recipe

* all_ingredients.py object to hold a master list of ingredients sourced from ingredient_list

* ingredient.pu object to hold information about individual ingredients

## TODO

generate CLI to:

* select recipes from an organized list
    
    * option for organizing by day of week

* selected recipes populate a shopping list

* feature to add a recipe - either step by step or querying a website and parsing it - also parsing a txt file?

* randomize function
