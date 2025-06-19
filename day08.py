from datetime import datetime

def add_expense():
    item = input("Enter item name: ")
    if item.lower() in ["exit", "quit", "q"]:
        return False

    amount = input("Enter amount: ")
    if amount.lower() in ["exit", "quit", "q"]:
        return False

    now = datetime.now()
    date = now.strftime("%Y-%m-%d")

    with open("Expense_tracker.txt", "a") as file:
        file.write(f"{date} | {item} - {amount}\n")
    print("Expense saved!\n")
    return True


def view_expenses(filter_type):
    today = datetime.now().date()
    current_week = today.isocalendar()[1]
    current_month = today.month
    current_year = today.year

    total = 0
    print(f"\n Expenses for: {filter_type.upper()}")

    try:
        with open("Expense_tracker.txt", "r") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue

                try:
                    date_part, entry = line.split(" | ")
                    date_obj = datetime.strptime(date_part, "%Y-%m-%d").date()

                    show = False
                    if filter_type == "day" and date_obj == today:
                        show = True
                    elif filter_type == "week" and date_obj.isocalendar()[1] == current_week and date_obj.year == current_year:
                        show = True
                    elif filter_type == "month" and date_obj.month == current_month and date_obj.year == current_year:
                        show = True

                    if show:
                        print(entry)
                        try:
                            amount = int(entry.split("-")[1].strip())
                            total += amount
                        except:
                            pass

                except ValueError:
                    continue

        print(f"\n Total Spent ({filter_type.upper()}): Ksh {total}\n")

    except FileNotFoundError:
        print("No expense file found yet.")




print(" Welcome to the Smart Expense Tracker")
while True:
    print("\nChoose an option:")
    print("1. Add Expense")
    print("2. View Today's Expenses")
    print("3. View This Week's Expenses")
    print("4. View This Month's Expenses")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        while add_expense():
            continue
    elif choice == "2":
        view_expenses("day")
    elif choice == "3":
        view_expenses("week")
    elif choice == "4":
        view_expenses("month")
    elif choice == "5":
        print("Goodbye! See you next time!")
        break
    else:
        print(" Invalid choice. Try again.")
