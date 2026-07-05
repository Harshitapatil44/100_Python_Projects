# Expense Forecasting Tool

expenses = []

n = int(input("Enter number of months: "))

for i in range(n):
    amount = float(input(f"Enter expense for month {i + 1}: "))
    expenses.append(amount)

total = sum(expenses)
average = total / n

print("\nExpense Summary")
print("---------------")
print("Total Expense:", total)
print("Average Monthly Expense:", round(average, 2))
print("Forecast for Next Month:", round(average, 2))
