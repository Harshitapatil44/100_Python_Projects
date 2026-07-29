import random

score = 0
wickets = 0
overs = 2

print("🏏 Cricket Score Simulator 🏏\n")

for over in range(1, overs + 1):
    print(f"\nOver {over}")
    
    for ball in range(1, 7):
        if wickets == 10:
            break

        outcome = random.choice([0, 1, 2, 3, 4, 6, "W"])

        if outcome == "W":
            wickets += 1
            print(f"Ball {ball}: Wicket! Total: {score}/{wickets}")
        else:
            score += outcome
            print(f"Ball {ball}: {outcome} runs. Total: {score}/{wickets}")

    if wickets == 10:
        print("\nAll Out!")
        break

print("\n----- Match Summary -----")
print(f"Final Score: {score}/{wickets}")
print(f"Overs Played: {over}")
