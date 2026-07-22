import random

words = ["python", "apple", "banana", "computer", "school", "laptop"]

word = random.choice(words)

letters = list(word)
random.shuffle(letters)
scrambled = "".join(letters)

print("=== Word Scramble Game ===")
print("Unscramble the word:", scrambled)

guess = input("Enter your guess: ").lower()

if guess == word:
    print("🎉 Correct! You Win!")
else:
    print("❌ Wrong!")
    print("The correct word was:", word)
