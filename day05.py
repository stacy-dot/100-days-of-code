print(" Welcome to the Pet Tracker App! ")

pets = ["cat", "dog", "chicken", "cat"]

fun_facts = (
    "Dogs are loyal animals.",
    "Cats love to nap in the sun.",
    "Chickens are surprisingly smart!",
    "Sheep have excellent memory!"
)

while True:
    print("\nChoose an option:")
    print("1. View all pets")
    print("2. Add a pet")
    print("3. Remove a pet")
    print("4. Check if a pet is in the list")
    print("5. Show unique pets")
    print("6. Show a random pet fun fact")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == "1":
        print("\n Your pets:")
        for pet in pets:
            print(f"- {pet}")

    elif choice == "2":
        new_pet = input("Enter the name of the pet to add: ")
        pets.append(new_pet)
        print(f"{new_pet} added to your pet list.")

    elif choice == "3":
        remove_pet = input("Enter the name of the pet to remove: ")
        if remove_pet in pets:
            pets.remove(remove_pet)
            print(f"{remove_pet} removed from your pet list.")
        else:
            print(f"{remove_pet} is not in your pet list.")

    elif choice == "4":
        check_pet = input("Enter the pet name to check: ")
        if check_pet in pets:
            print(f"Yes, you have a {check_pet}!")
        else:
            print(f"No, {check_pet} is not on your list.")

    elif choice == "5":
        unique_pets = set(pets)
        print("\n Unique pets (no duplicates):")
        for pet in unique_pets:
            print(f"- {pet}")

    elif choice == "6":
        import random
        fact = random.choice(fun_facts)
        print(f"\n Fun Fact: {fact}")

    elif choice == "7":
        print("Goodbye! Thanks for using Pet Tracker.")
        break

    else:
        print("Invalid choice. Please try again.")

