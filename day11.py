'''import matplotlib.pyplot as plt

expenses=[
    {"item": "Rent", "amount": 15000},
    {"item": "food", "amount":6000},
    {"item": "Transport", "amount":5000},
    {"item": "internet", "amount":2000}
    
]

def show_barchart():
    items=[expense["item"] for expense in expenses]
    amount=[expense["amount"] for expense in expenses]

    plt.figure (figsize=(8,5))
    plt.bar(items,amount,color='skyblue')
    plt.title("Monthly Expenses")
    plt.xlabel("Category")
    plt.ylabel("Amount(KSH)")
    plt.tight_layout()
    plt.show()

def show_pie_chart():
    items = [expense["item"] for expense in expenses]
    amounts = [expense["amount"] for expense in expenses]

    plt.figure(figsize=(6, 6))
    plt.pie(amounts, labels=items, autopct='%1.1f%%', startangle=140)
    plt.title("Expense Distribution")
    plt.tight_layout()
    plt.show()


show_barchart()
show_pie_chart()'''

import matplotlib.pyplot as plt

expenses=[]

def add_expense():
    while True:
        item=input("Enter item name(or done to finish):")
        if item.lower()=="done":
            break
        try:
            amount=float(input(f"Amount spent on {item}:"))
            expenses.append({"item":item,"amount":amount})
        except ValueError:
            print("Invalid amount.Try again!")

def show_barchart():
    if not expenses:
        print("No data to display. Add expenses first.")
        return
    amount=[expense["amount"] for expense in expenses]
    item=[expense["item"] for expense in expenses]
    total=sum(expense["amount"] for expense in expenses)


    plt.figure(figsize=(7,4))
    plt.bar(item, amount,color=['#FF6F61', '#6B5B95', '#88B04B', '#F7CAC9'])
    plt.title(f"Monthly Expeses-Total:ksh{total}")
    plt.xlabel("item")
    plt.ylabel("amount")
    plt.tight_layout()
    plt.show()

def show_piechart():
    if not expenses:
        print("No data to display.Add expenses first!")
    item=[expense["item"] for expense in expenses]
    amount=[expense["amount"] for expense in expenses]
    total=sum(amount)

    plt.figure(figsize=(5,5))
    plt.pie(amount,labels=item,autopct='%1.1f%%' ,startangle=140)
    plt.title(f"Monthly Expenditure-Total:KSH{total}")
    plt.tight_layout()
    plt.show()

while True:
    print("---Expense menu---")
    print("1.Add expenses")
    print("2.Show bar chart")
    print("3.Show pie chart")
    print("4.exit")
    choice=input("Choose option 1-4:")

    if choice=="1":
        add_expense()
    elif choice=="2":
        show_barchart()
    elif choice=="3":
        show_piechart()
    elif choice=="4":
        print("Goodbye!")
        break
    else:
        print("Invalid option!Try again.")