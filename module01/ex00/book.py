from recipe import Recipe
from datetime import datetime

class Book:

    def __init__(self, name):
        self.recipes = []
        self.name = name
        self.creation_date = datetime.now()
        self.last_update = datetime.now()
        self.recipe_list = ['starter', 'lunch', 'dessert']

    def add_recipe(self, recipe):
        try:
            if isinstance(recipe, Recipe) and (len([str(recipe) for rec in self.recipes if rec.name == recipe.name]) == 0):
                print(str(recipe))
                self.recipes.append(recipe)
                print('Recipe for {name} added to book\n'.format(name=recipe.name))
                self.last_update = datetime.now()
            else:
                raise

        except:
            print('Error adding recipe to book\n')

    def get_recipe_by_name(self, name):
        try:
            rec = [str(recipe) for recipe in self.recipes if recipe.name == name]
            if len(rec) == 1:
                print(str(rec[0]))
            else:
                raise
        except:
            print("No recipe with name {name}\n".format(name=name))

    def get_recipes_by_type(self, type):
        try:
            rec = [str(recipe) for recipe in self.recipes if recipe.recipe_type == type and type in self.recipe_list]
            if len(rec) >= 1:
                print("\n\n".join(rec))

            else:
                raise
        except:
            print("No recipes with type {type}\n".format(type=type))


    def show_recipes(self):
        print("\n\n".join([str(recipe) for recipe in self.recipes]))
