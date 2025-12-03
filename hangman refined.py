import random
n = random.randint(1, 100)
guesses = 0
a = 0
while (a != n):
    guesses += 1
    a = int(input("Guess the number: "))
    if (a>n):
        print("Lower number please.")
    elif (a<n):
        print("Higher number please")
print(f"You have guessed the number {n} in {guesses} attempts.")


import random


HANGMAN = [
    '________',
    '|       |',
    '|       O',
    '|       |',
    '|      /|\ ',
    '|       |',
    '|      / \ '
]

WORDS = [
    'CASA', 'CARRO', 'MONO', 'ESTERNOCLEIDOMASTOIDEO', 'PYTHON', 'DJANGO',
    'MILTON', 'LENIS', 'SWAPPS', 'LOGIA', 'UNITTESTING'
]

class Hangman():
    """
    The hangman game class with his methods
    """

    def __init__(self, word_to_guess):
        self.failed_attempts = 0
        self.word_to_guess = word_to_guess
        self.game_progress = list('_' * len(self.word_to_guess))

    def find_indexes(self, letter):
        """
        Method that takes a letter and returns a list with his indexes in
        the word to guess
        :param letter: String, Letter to find his indexes
        """
        return [i for i, char in enumerate(self.word_to_guess) if letter == char]

    def is_invalid_letter(self, input_):
        """
        Method to validate if an user input is not just a letter (it means the
        input is a number or a text with more than 1 char)
        :param input_: String, user input to be validated
        """
        return input_.isdigit() or (input_.isalpha() and len(input_) > 1)

    def print_game_status(self):
        """
        Method to print the word to guess blankspaces with the remaining
        attempts and the guessed letters
        """
        # We append withespaces both sides to make the game look prettier
        print('\n')
        print('\n'.join(HANGMAN[:self.failed_attempts]))
        print('\n')
        print(' '.join(self.game_progress))

    def update_progress(self, letter, indexes):
        """
        Method to update the game progress with the guessed letters
        :param letter: String, Letter to be added to the game progress
        :param indexes: List, found occurrences (as indexes) of the given
                        letter in the word
        """
        for index in indexes:
            self.game_progress[index] = letter

    def get_user_input(self):
        user_input = input('\nPlease type a letter: ')
        return user_input

    def play(self):
        """
        Method to play the game, it prompts the user for a letter and plays
        the game until the user guesses the word or lose his attempts
        """
        while self.failed_attempts < len(HANGMAN):
            self.print_game_status()
            user_input = self.get_user_input()

            # Validate the user input
            if self.is_invalid_letter(user_input):
                print('¡The input is not a letter!')
                continue
            # Check if the letter is not already guessed
            if user_input in self.game_progress:
                print('You already have guessed that letter')
                continue

            if user_input in self.word_to_guess:
                indexes = self.find_indexes(user_input)
                self.update_progress(user_input, indexes)
                # If there is no letter to find in the word
                if self.game_progress.count('_') == 0:
                    print('\n¡Yay! You win!')
                    print('The word is: {0}'.format(self.word_to_guess))
                    quit()
            else:
                self.failed_attempts += 1
        print("\n¡OMG! You lost!")

if __name__ == '__main__':
    word_to_guess = random.choice(WORDS)
    hangman = Hangman(word_to_guess)
    hangman.play()




import random

Words = ["RAJASTHAN", "HUMAN", "CODE", "LAPTOP", "INDIA"]

class hangman:
    '''
    A class to represent and manage a game og hangman.
    '''
    def __init__(self, wordToGuess):
        self.word = wordToGuess.upper()
        self.guessedLetters = set()
        pass

    def displayWord(self):
        """
        Generates the word to display to the player, with unguessed letters as underscore.
        """
        display = ""
        for x in self.word:
            if x in self.guessedLetters:
                display += x + " "  
            else:
                desplay += "_ "
        return display.strip()
    
    def guessLetter(self, x):
        """
        Processes a single letter (x) guess and updates the game's state.
        Returns true if the guess was correct, false otherwise.
        """

        # add the guessed letter to our set
        


# main part of the program to run the game
if __name__ == "__main__":
    # pick a randome word from the list.
    secretWord = random.choice(Words)

    # create an object from the hangman class.
    # this creates a new, specific game instance or object based on the blueprint

    game = hangman(secretWord)

    print("Welcome to Hangman!")


