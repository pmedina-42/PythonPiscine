from book import Book
from recipe import Recipe

if __name__ == '__main__':
    recipe = Recipe(name='tarta de queso', c_l=2, c_t=60, i=['cosas', 'azucar', 'queso'], r_t='dessert')
    sw = Recipe(name='sandwich', c_l=1, c_t=5, i=['pan', 'jamon', 'queso'], r_t='*')
    sw2 = Recipe(name='sandwich', c_l=1, c_t=5, i=['agua', 'fideos'], r_t='*')
    book = Book('cookbook')
    book.add_recipe(recipe)
    book.add_recipe(sw)
    book.add_recipe(sw2)
    book.add_recipe(4)
    book.show_recipes()
    book.get_recipe_by_name('culo')
    book.get_recipes_by_type('dessert')
    book.get_recipes_by_type('cena')
    print(book.creation_date)
    print(book.last_update)
