from book import Book
from recipe import Recipe

if __name__ == '__main__':
    recipe = Recipe(name='tarta de queso', c_l=2, c_t=60, i=['cosas', 'azucar', 'queso'], r_t='dessert')
    flan = Recipe(name='flan', c_l=2, c_t=60, i=['cosas', 'azucar', 'huevo'], r_t='dessert')
    sw = Recipe(name='sandwich', c_l=1, c_t=5, i=['pan', 'jamon', 'queso'], r_t='*')
    sw2 = Recipe(name='sandwich', c_l=1, c_t=5, i=['agua', 'fideos'], r_t='*')

    print('Creating cookbook\n-------------------------------')
    book = Book('cookbook')

    print('Adding tarta de queso\n...............................')
    book.add_recipe(recipe)

    print('Adding flan\n...............................')
    book.add_recipe(flan)

    print('Adding sandwich\n...............................')
    book.add_recipe(sw)

    print('Adding 2nd sandwich\n...............................')
    book.add_recipe(sw2)

    print('Adding 42 to book\n--------------------------------')
    book.add_recipe(4)

    print('Show recipes output\n--------------------------------')
    book.show_recipes()

    print('Get "culo" recipe\n--------------------------------')
    book.get_recipe_by_name('culo')

    print('Get "tarta de queso" recipe\n--------------------------------')
    book.get_recipe_by_name('tarta de queso')

    print('Get "dessert" recipes\n--------------------------------')
    book.get_recipes_by_type('dessert')

    print('Get "cena" recipes\n--------------------------------')
    book.get_recipes_by_type('cena')

    print('Show book dates\n--------------------------------')
    print('Creation time: {c}'.format(c=book.creation_date))
    print('Modification time: {c}'.format(c=book.last_update))
