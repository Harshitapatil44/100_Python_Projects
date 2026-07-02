income = float(input("Enter your monthly income: "))

num = int(input("How many expenses do you want to add? "))

total_expense = 0

for i in range(num):
    expense = float(input(f"Enter expense {i + 1}: "))
    total_expense += expense

balance = income - total_expense

print("\n----- Budget Summary -----")
print("Total Income   :", income)
print("Total Expenses :", total_expense)
print("Remaining      :", balance)

if balance > 0:
    print("You are within your budget.")
elif balance == 0:
    print("Your budget is exactly balanced.")
else:
    print("You have exceeded your budget.")
