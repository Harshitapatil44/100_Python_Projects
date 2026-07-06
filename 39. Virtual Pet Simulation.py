class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.happiness = 5

    def feed(self):
        if self.hunger > 0:
            self.hunger -= 1
        print(f"{self.name} has been fed.")

    def play(self):
        self.happiness += 1
        self.hunger += 1
        print(f"You played with {self.name}.")

    def status(self):
        print("\n--- Pet Status ---")
        print("Name:", self.name)
        print("Hunger Level:", self.hunger)
        print("Happiness Level:", self.happiness)

pet_name = input("Enter your pet's name: ")
pet = Pet(pet_name)

while True:
    print("\n1. Feed Pet")
    print("2. Play with Pet")
    print("3. Check Status")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        pet.feed()
    elif choice == "2":
        pet.play()
    elif choice == "3":
        pet.status()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
