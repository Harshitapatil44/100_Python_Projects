import random

tickets = int(input("How many tickets do you want? "))

for i in range(tickets):
    numbers = random.sample(range(1, 50), 6)
    numbers.sort()
    print(f"Ticket {i + 1}: {numbers}")
