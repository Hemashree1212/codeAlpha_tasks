import random

# List of predefined words
words = ["apple", "tiger", "house", "chair", "plant"]

# Select random word
word = random.choice(words)

guessed_letters = []
incorrect_guesses = 0
max_guesses = 6

display_word = ["_"] * len(word)

print("Welcome to Hangman Game!")

while incorrect_guesses < max_guesses and "_" in display_word:
    print("\nWord:", " ".join(display_word))
    guess = input("Enter a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct guess!")
        for i in range(len(word)):
            if word[i] == guess:
                display_word[i] = guess
    else:
        incorrect_guesses += 1
        print("Wrong guess!")
        print("Remaining guesses:", max_guesses - incorrect_guesses)

if "_" not in display_word:
    print("\nCongratulations! You guessed the word:", word)
else:
    print("\nGame Over! The word was:", word)