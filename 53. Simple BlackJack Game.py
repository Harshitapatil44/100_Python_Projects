import random

print("***** BLACKJACK GAME *****")

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

player = random.choice(cards) + random.choice(cards)
dealer = random.choice(cards) + random.choice(cards)

print("Your total:", player)
print("Dealer's first card:", dealer - random.choice(cards))

while True:
    if player > 21:
        print("You busted! Dealer wins.")
        break

    choice = input("Hit or Stand? (h/s): ").lower()

    if choice == "h":
        card = random.choice(cards)
        player += card
        print("You got:", card)
        print("Your total:", player)
    else:
        while dealer < 17:
            dealer += random.choice(cards)

        print("\nDealer total:", dealer)

        if dealer > 21:
            print("Dealer busted! You win!")
        elif player > dealer:
            print("You win!")
        elif player < dealer:
            print("Dealer wins!")
        else:
            print("It's a tie!")

        break
