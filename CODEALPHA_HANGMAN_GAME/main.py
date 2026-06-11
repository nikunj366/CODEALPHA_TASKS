import random
words = ["apple", "mango", "penguin", "grapes", "horse"]

word = random.choice(words)


guessed = ["_"] * len(word)

attempts = 6

guessed_letters = []

print("--------------------------")
print(" Welcome to Hangman Game ")
print("--------------------------")
print("Guess the word:")
print(" ".join(guessed))

while attempts > 0 and "_" in guessed:

    guess = input("\nEnter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed this letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct Guess!")

        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
    else:
        attempts -= 1
        print(f"Wrong Guess! Attempts left: {attempts}")
        print("Word:", " ".join(guessed))

if "_" not in guessed:
    print("\n Congratulations!")
    print(f"You guessed the word: {word}")

else:
    print("\n Game Over!")
    print(f"The correct word was: {word}")