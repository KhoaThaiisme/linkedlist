# You have a recipe that serves a certain number of people, and you want to create a function that takes this recipe, the number of servings it produces, and the number of people to serve as input, and adjusts the recipe quantities accordingly.
# Write a Python function called adjust_recipe() that takes three arguments:
# 1) recipe (dictionary):
# A dictionary representing the original recipe.
# Each key-value pair should contain the following information:
# ingredient (string): The name of the ingredient.
# quantity (float): The quantity of the ingredient required for the recipe, in cups.
# 2) original_servings (integer): An integer representing the number of people the original recipe serves.
# 3) new_servings (integer): An integer representing the number of people to serve with the adjusted recipe.
# The function should return a new dictionary containing the adjusted ingredient quantities.
# Here’s an example of the input and output :
# base_recipe = {
#       ‘flour’: 2,
#       ‘sugar’: 1,
#       ‘butter’: 0.5,d
#       ‘eggs’: 2
# }
# INPUT : (base_recipe, 4, 6) - This means the base recipe is made to serve 4 people and you want
# to adjust it for 6 people.
# OUTPUT: {
#     ‘flour’: 3,
#     ‘sugar’: 1.5,
#     ‘butter’: 0.75,
#     ‘eggs’: 3
#         }

# empty dictionary to give out adjusted ingredients 

# def adjust_recipe(recipe, original_serving, new_servings):
#     adjusted_recipe = {}
#     one_portion = 0
#     for e in recipe[e]:
#         one_portion += e / original_serving
#         adjusted_recipe[e] = one_portion*new_servings
#     return adjusted_recipe


# base_recipe = {
#     'flour': 2,       
#     'sugar': 1,
#     'butter': 0.5,
#     'eggs': 2
# }

# original_servings = 4
# new_servings = 2

# print(adjust_recipe(base_recipe, 4, 6))



def adjust_recipe(recipe, original_serving, new_serving):
    new_serving_dictionary = {}
    for ingredient, amount in recipe.items():
        amount_per_serving = amount / original_serving
        new_serving_dictionary[ingredient] = amount_per_serving * new_serving
    return new_serving_dictionary
# ///////// Todd's////////
def adjust_recipe(this_recipe, base_servings, new_servings):
    multiplyer = round(float(new_servings/base_servings),2)

    for ele in this_recipe:
        this_recipe[ele] = round(this_recipe[ele]*multiplyer,2)

adjust_recipe(a_recipe, 4,6)

print(a_recipe)