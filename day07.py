habits=[]
completed=[]

def show_menu():
    print("\nHabit Tracker Menu:")
    print("1. View Habits")
    print("2. Add Habit")
    print("3. Mark Habit as Complete")
    print("4. View completed habits")
    print("5. Exit")

while True:
    show_menu()
    choice=input("Enter a choice between (1-5):")
    if choice == "1":
        if habits:
            print("Your habits:")
            for habit in habits:
                print(f"- {habit}")
        else:
            print("No habits added yet.")

    elif choice == "2":
        new_habit = input("Enter the new habit: ")
        habits.append(new_habit)
        print(f"'{new_habit}' added.")

    elif choice == "3":
        habit_name = input("Enter the habit to mark as complete: ")
        if habit_name in habits:
            habits.remove(habit_name)
            completed.append(habit_name)
            print(f"'{habit_name}' marked as complete.")
        else:
            print("Habit not found.")

    elif choice == "4":
        print("Completed habits:")
        for done in completed:
            print(f"- {done}")

    elif choice == "5":
        print("Goodbye! Keep building good habits.")
        break

    else:
        print("Invalid choice. Please try again.")