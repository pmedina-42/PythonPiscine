import random

class guess_game:

    def __init__(self):
        self.num = random.randrange(0, 100)
        self.print_header()
        self.won = False
        self.exit = False
        self.att = 0
        while not self.won and not self.exit:
            self.ask_for_input()
        if self.won:
            print("You won in {a} attempts!".format(a=self.att))

    def ask_for_input(self):
        i = input("What's your guess between 1 and 99?\n>> ")
        self.check_input(i)

    def check_input(self, i):
        try:
            if str(i) == "exit":
                self.exit = True
                return
            # TODO if input is exit case
            print(("Too low!","Too high!", "Congratulations, you've got it!", "The answer to the ultimate question of life, the universe and everything is 42.")
                  [(int(i) >= self.num) + (int(i) == self.num) + (int(i) == 42)])
            self.att += 1
            if ((int(i) >= self.num) + (int(i) == self.num)) == 2:
                self.won = True

        except:
            print("Bad input")

    def print_header(self):
        print("This is an interactive guessing game!")
        print("You have to enter a number between 1 and 99 to find out the secret number.")
        print("Type 'exit' to end the game.")
        print("Good luck!\n")


def main():
    game = guess_game()

if __name__ == '__main__':
    main()