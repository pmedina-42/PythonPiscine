class Recipe:

    def __str__(self):
        try:
            full_recipe = [
                'Recipe for {n}'.format(n=self.name),
                'Cooking level: {l}'.format(l=self.cooking_lvl),
                'Cooking time: {t}'.format(t=self.cooking_time),
                'Ingredients {i}'.format(i=", ".join(self.ingredients)),
                'Description: {d}'.format(d=self.description),
                'Recipe type: {r}'.format(r=self.recipe_type)
            ]
            return "\n".join(full_recipe)
        except:
            return'Cannot convert recipe to string'
    def __init__(self, **kwargs):
        try:
            if all(key in kwargs for key in ('name', 'c_l', 'c_t', 'i', 'r_t')):
                self.name = kwargs['name']
                self.cooking_lvl = kwargs['c_l']
                self.cooking_time = kwargs['c_t']
                self.ingredients = kwargs['i']
                self.description = 'desc' in kwargs and kwargs['desc'] or ''
                self.recipe_type = kwargs['r_t']
            else:
                raise

        except:
            print("Error")



