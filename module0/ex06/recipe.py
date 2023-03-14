class recipe:

    def __init__(self):
        self.cookbook = {
            'bocadillo': {
                'ingredients': ['jamon', 'pan', 'queso', 'tomate'],
                'meal': 'almuerzo',
                'prep_time': 10
            },
            'tarta': {
                'ingredients': ['harina', 'azucar', 'huevos'],
                'meal': 'postre',
                'prep_time': 60
            },
            'ensalada': {
                'ingredients': ['aguacate', 'rucula', 'tomates', 'espinacas'],
                'meal': 'almuerzo',
                'prep_time': 15
            }
        }

        self.NOT_FOUND = '\nRecipe name {s} not found in cookbook\n'


    def get_recipes(self):
        print("Cookbook Recipes: \n\n\t- {s}\n".format(s="\n\t- ".join(self.cookbook)))

    def get_recipe(self, r):
        try:
            print("\nRecipe for {s}:\n Ingredients list: {st}.".format(s=r, st=", ".join(self.cookbook[r]['ingredients'])))
            print("  To be eaten for {s}.".format(s=self.cookbook[r]['meal']))
            print("  Takes {s} minutes of cooking.\n".format(s=self.cookbook[r]['prep_time']))

        except:
            print(self.NOT_FOUND.format(s=r))

    def delete_recipe(self, r):
        try:
            del self.cookbook[r]
            print("\n{s} recipe deleted\n".format(s=r))
        except:
            print(self.NOT_FOUND.format(s=r))

    def create_recipe(self, name, ingredients, meal, prep_time):
        try:
            self.cookbook[name] = {
                'ingredients': ingredients,
                'meal': meal,
                'prep_time': prep_time
            }
        except:
            print("\nRecipe with name {s} already exists in cookbook.\n".format(s=r))


def print_header():
    print("Welcome to the Python Cookbook!")
    print("List of available options:")
    print("\t1: Add a recipe")
    print("\t2: Delete a recipe")
    print("\t3: Print a recipe")
    print("\t4: Print the cookbook")
    print("\t5: Quit\n")

def get_args_and_create(rec):
    name = input("\n>> Enter a name:\n")
    ingredients = [input("\n>> Enter the ingredients:\n")]
    while True:
        i = input()
        if i != "":
            ingredients += [i]
        else:
            break
    meal = input("\n>> Enter meal type:\n")
    prep_time = input("\n>> Enter a preparation time:\n")
    rec.create_recipe(name, ingredients, meal, prep_time)


def main():

    print_header()
    rec = recipe()
    run = True
    while run:
        opt = input("\nPlease select an option: \n>> ")
        if not opt.isnumeric():
            continue
        match int(opt):
            case 1:
                get_args_and_create(rec)
            case 2:
                r = input("\nPlease enter a recipe name to delete:\n>> ")
                rec.delete_recipe(r)
            case 3:
                r = input("\nPlease enter a recipe name to get its details:\n>> ")
                rec.get_recipe(r)
            case 4:
                rec.get_recipes()
            case 5:
                print("\nBye bye!\n")
                run = False



if __name__ == '__main__':
    main()