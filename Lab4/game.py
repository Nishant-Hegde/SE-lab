import random
from words import WORDS
from feedback import evaluate


class WordleGame:
    def __init__(self, length=5):
        if length not in {4, 5, 6}:
            raise ValueError("Word length must be 4, 5, or 6.")

        self.length = length
        self.target = random.choice(
            [word for word in WORDS if len(word) == length]
        )
        self.history = []

    def display_history(self):
        print("\nGuess History:")
        for guess, feedback in self.history:
            print(f"{guess}: {' '.join(feedback)}")
        print()

    def display_summary(self, won):
        print("\n===== Game Summary =====")
        print(f"Word length: {self.length}")
        print(f"Guesses used: {len(self.history)}")

        if won:
            print("Result: Won")
        else:
            print("Result: Lost")

        print(f"Target word: {self.target}")
        print("========================")

    def run(self):
        print(f"Wordle — {self.length} letters, 6 guesses.")

        accepted_guesses = 0

        while accepted_guesses < 6:
            guess = input("> ").strip().lower()

            if guess == "q":
                print("Game quit.")
                self.display_summary(False)
                return

            if len(guess) != self.length or not guess.isalpha():
                print("Enter a valid word of the required length.")
                continue

            accepted_guesses += 1

            feedback = evaluate(self.target, guess)
            self.history.append((guess, feedback))

            print(" ".join(feedback))

            self.display_history()

            if guess == self.target:
                print("Solved!")
                self.display_summary(True)
                return

        print("Out of guesses!")
        self.display_summary(False)