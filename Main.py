import random
import string

print("""H A N G M A N""")


class Game:
    def __init__(self, num_chances=8):
        self.num_chances = num_chances
        pass

    def play(self, word):
        holder = "".join(list("-" * len(word)))  # Grid display
        all_letters = set()  # Set to keep guessed letters
        while self.num_chances > 0:
            print(f"\n{holder}")
            if "-" not in list(holder):  # Check if finished
                return "You guessed the word!\nYou survived!"
            guess = input("Input a letter: ")
            loc = [pos for pos, char in enumerate(word) if char == guess]
            if self.check_word(guess, loc, all_letters):
                holder = list(holder)  # Correct
                for n in loc:
                    holder[n] = guess
                holder = "".join(holder)
                all_letters.add(guess)

        return "You are hanged!"

    def check_word(self, guess, loc, all_letters):
        if guess in all_letters:  # Same letter?
            print("You already typed this letter")
            return False
        if len(guess) > 1:  # Single letter?
            print("You should input a single letter")
            return False
        if guess not in string.ascii_lowercase:  # Letter lowercase?
            print("It is not an ASCII lowercase letter")
            return False
        if not loc:  # Wrong letter?
            self.num_chances -= 1
            print("No such letter in the word")
            all_letters.add(guess)
            return False
        return True

    def choose_word(self, words=['python', 'java', 'kotlin', 'javascript']):
        return random.choice(words)


game = Game()

while True:
    choice = input("Type \"play\" to play the game, \"exit\" to quit: ")
    if choice == "play":
        print(game.play(word=game.choose_word()))
    elif choice == "exit":
        break
