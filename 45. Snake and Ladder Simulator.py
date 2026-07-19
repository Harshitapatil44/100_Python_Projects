import random

player = 0

board = {
    4: 14,
    9: 31,
    20: 38,
    28: 84,
    40: 59,
    51: 67,
    63: 81,

    17: 7,
    54: 34,
    62: 19,
    64: 60,
    87: 24,
    93: 73,
    95: 75,
    99: 78
}

print("Welcome to Snake and Ladder!")

while player < 100:
    input("Press Enter to roll the dice...")
    dice = random.randint(1, 6)
    print("You rolled:", dice)

    if player + dice <= 100:
        player += dice

    if player in board:
        if board[player] > player:
            print("Ladder! Climb up.")
        else:
            print("Snake! Slide down.")
        player = board[player]

    print("Current Position:", player)

    if player == 100:
        print("🎉 Congratulations! You won!")
        break
