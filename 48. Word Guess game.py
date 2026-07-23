import random

words = ["apple", "python", "banana", "laptop", "school", "flower"]

word = random.choice(words)
guessed = ["_"] * len(word)
attempts = 6

print("=== Word Guess Game ===")

while attempts > 0 and "_" in guessed:
    print("\nWord:", " ".join(guessed))
    guess = input("Enter a letter: ").lower()

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
        print("Correct!")
    else:
        attempts -= 1
        print("Wrong! Attempts left:", attempts)

if "_" not in guessed:
    print("\n🎉 You Win!")
    print("The word was:", word)
else:
    print("\n😢 You Lose!")
    print("The word was:", word)
