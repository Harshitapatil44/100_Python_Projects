import time

work = int(input("Enter work time (minutes): "))
break_time = int(input("Enter break time (minutes): "))

print("\nWork Session Started")

for i in range(work * 60, 0, -1):
    mins = i // 60
    secs = i % 60
    print(f"\r{mins:02}:{secs:02}", end="")
    time.sleep(1)

print("\nWork Session Complete!")

print("Break Started")

for i in range(break_time * 60, 0, -1):
    mins = i // 60
    secs = i % 60
    print(f"\r{mins:02}:{secs:02}", end="")
    time.sleep(1)

print("\nBreak Complete!")
