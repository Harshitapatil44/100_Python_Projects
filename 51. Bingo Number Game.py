import random

print("Welcome to Bingo Number Generator")

numbers = list(range(1, 91))
random.shuffle(numbers)

while numbers:
    input("\nPress Enter to draw a number...")
    print("Number:", numbers.pop())

print("\nAll bingo numbers have been drawn!")
