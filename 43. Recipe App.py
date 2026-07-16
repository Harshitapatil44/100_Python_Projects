recipes = {
    "Tea": "Boil water, add tea powder, milk, sugar.",
    "Maggi": "Boil water, add Maggi and tastemaker, cook for 2 minutes.",
    "Sandwich": "Place vegetables between bread slices and toast."
}

while True:
    print("\n=== Recipe App ===")
    print("1. View Recipes")
    print("2. Add Recipe")
    print("3. Search Recipe")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("\nRecipes:")
        for name in recipes:
            print("-", name)

    elif choice == "2":
        name = input("Enter recipe name: ")
        recipe = input("Enter recipe steps: ")
        recipes[name] = recipe
        print("Recipe added successfully!")

    elif choice == "3":
        name = input("Enter recipe name: ")
        if name in recipes:
            print("\nRecipe for", name)
            print(recipes[name])
        else:
            print("Recipe not found!")

    elif choice == "4":
        print("Thank you for using Recipe App!")
        break

    else:
        print("Invalid choice! Please try again.")
