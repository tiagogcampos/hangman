import requests


class HangmanGame:

    def __init__(self):
        self.new_game()

    def new_game(self):
        self.word = self.get_word().lower()
        self.errors = 7
        self.guessed = '_' * len(self.word)
        self.used = []
        self.start_game()
        self.play_again()

    def find(self, ch):
        for i, letter in enumerate(self.word):
            if letter == ch:
                yield i

    def get_word(self):
        r = requests.get('https://random-word-api.herokuapp.com/word?number=1')
        if r.status_code == 200:
            r = r.json()
            return r[0]

    def start_game(self):
        while self.errors >= 0:
            self.move()
        print(f"The word is: {self.word}")
        return

    def play_again(self):
        r = input("Play again? (Y,n) ")
        if r == 'y' or r == 'Y':
            self.new_game()

    def move(self):
        print(self.guessed)
        letter = input("Letter: ")
        if letter == '':
            return
        letter = letter[0].lower()
        if letter in self.word and letter not in self.used:
            indexes = self.find(letter)
            print("Right")
            for i in list(indexes):
                l = list(self.guessed)
                l[i] = self.word[i]
                self.guessed = ''.join(l)
            print(self.guessed)
            self.used.append(letter)
        else:
            print("Wrong")
            print(f"Lives left: {self.errors}")
            self.errors -= 1

        if '_' not in self.guessed:
            print("You won!")
            return


game = HangmanGame()
