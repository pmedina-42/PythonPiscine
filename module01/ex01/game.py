

class GotChatacter:

    def __init__(self, n='John Doe', alive=True):
        self.first_name = n
        self.is_alive = alive


class Lannister(GotChatacter):
    """A class representing the Lannister family"""
    def __init__(self, name='John Doe'):
        super().__init__(n=name, alive=True)
        self.family_name = 'Lannister'
        self.house_words = 'A Lannister pays his debts'


    def print_house_words(self):
        print(self.house_words)
    def die(self):
        self.is_alive = False


#if __name__ == '__main__':
#    tyrion = Lannister('Tyrion')
#    print(tyrion.__dict__)
#    tyrion.print_house_words()
#    print(tyrion.is_alive)
#    tyrion.die()
#    print(tyrion.is_alive)
#+    print(tyrion.__docs__)
