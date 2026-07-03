import random

recipes = {
    "Breakfast": [
        "Poha",
        "Upma",
        "Vegetable Sandwich"
    ],
    "Lunch": [
        "Dal Rice",
        "Paneer Curry with Roti",
        "Veg Pulao"
    ],
    "Dinner": [
        "Khichdi",
        "Veg Fried Rice",
        "Pasta"
    ],
    "Snacks": [
        "Bhel Puri",
        "Maggi",
        "Corn Chaat"
    ]
}

print("Recipe Generator")
print("1. Breakfast")
print("2. Lunch")
print("3. Dinner")
print("4. Snacks")

choice = input("Enter your choice: ")

if choice == "1":
    print("Recipe:", random.choice(recipes["Breakfast"]))
elif choice == "2":
    print("Recipe:", random.choice(recipes["Lunch"]))
elif choice == "3":
    print("Recipe:", random.choice(recipes["Dinner"]))
elif choice == "4":
    print("Recipe:", random.choice(recipes["Snacks"]))
else:
    print("Invalid choice!")
