# Simple Recipe Recommender System

recipes = {
    "Pasta": ["pasta", "tomato", "cheese"],
    "Vegetable Sandwich": ["bread", "tomato", "cucumber", "cheese"],
    "Paneer Curry": ["paneer", "onion", "tomato"],
    "Fruit Salad": ["apple", "banana", "orange"],
    "Omelette": ["egg", "onion", "cheese"]
}

ingredient = input("Enter an ingredient: ").lower()

found = False

print("\nRecommended Recipes:")

for recipe, ingredients in recipes.items():
    if ingredient in ingredients:
        print("-", recipe)
        found = True

if not found:
    print("No recipes found with that ingredient.")
