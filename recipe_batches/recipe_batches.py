#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    max_batches = -1
    for item, quantity in recipe.items():
        if item in ingredients:
            if ingredients[item] / quantity < max_batches or max_batches == -1:
                max_batches = ingredients[item] / quantity
        else:
            return 0
    if max_batches == -1:
        return 0
    else:
        return int(max_batches)  # using int() truncates the float here


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
