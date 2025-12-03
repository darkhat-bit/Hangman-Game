import random

class Hangman:
    def __init__(self, word):
        self.word = word
        self.guessed_letters = set()
        self.attempts_left = 7
    
    def guess(self, letter):
        letter = letter.lower()
        if letter in self.guessed_letters:
            print("Letter already guessed.")
        elif letter in self.word:
            self.guessed_letters.add(letter)
            print("Good Guess!")
        else:
            self.guessed_letters.add(letter)
            self.attempts_left -= 1
            print(f"Wrong Guess. \nAttempt Left: {self.attempts_left}")

    def display_word(self):
        displayed = ""
        for char in self.word:
            if char in self.guessed_letters:
                displayed += char + " "
            else:
                displayed += "_ "
        print(displayed.strip())
    
    def is_won(self):
        return all(char in self.guessed_letters for char in self.word)

    def is_lost(self):
        return self.attempts_left <= 0

def main():
    WORDS = ["python", "code", "hackathon", "stock", "money"]
    word = random.choice(WORDS)
    game = Hangman(word)

    while not (game.is_won() or game.is_lost()):
        game.display_word()
        guess = input(f"\nEnter Your Guess: ")
        game.guess(guess)

    if game.is_won():
        print("Congratualation, You Guessed The Word.")
    else:
        print("Game over. The word was", game.word)

main()