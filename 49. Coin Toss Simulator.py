import random

print("=== Coin Toss Simulator ===")

while True:
    toss = random.choice(["Heads", "Tails"])
    print("Result:", toss)

    again = input("Toss again? (yes/no): ").lower()

    if again != "yes":
        print("Thanks for playing!")
        break
