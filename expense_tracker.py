import datetime
import json
expenses = []
def save_expenses():
  with open("expenses.json", "w") as file:
    json.dump(expenses, file)
def load_expenses():
    global expenses
    try:
        with open("expenses.json", "r") as file:
            expenses = json.load(file)

    except FileNotFoundError:
        expenses = []
load_expenses()
def add_expenses(amount, category, note):
  expense = {
    "amount": amount,
    "category": category,
    "note": note,
    "date": datetime.date.today()
  }
  
  expenses.append(expense)
  save_expenses()
  print("Expense added successfully!")

def view_expense():
  for expense in expenses:
    print("Amount   :", expense["amount"])
    print("Category :", expense["category"])
    print("Note     :", expense["note"])
    print("Date :", expense["date"])
    print("--------------------")
def total_expenses():
    total = 0

    for expense in expenses:
        total += expense["amount"]

    print("Total Expenses:", total)

def filter_by_category():
    category = input("Enter category to filter: ")

    found = False

    for expense in expenses:
        if expense["category"].lower() == category.lower():
            print(expense)
            found = True

    if not found:
        print("No expenses found in this category.")
while True:
    print("\n--- Expense Tracker ---")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Summary")
    print("4. Filter by Category")
    print("5. Exit")

    choice = input("Enter your choice: ")
    
    if choice == "1":
        amount = int(input("Enter your amount: "))
        category = input("Enter your category: ")
        note = input("Enter the short note: ")
        add_expenses(amount, category, note)

    elif choice == "2":
        view_expense()

    elif choice == "3":
        total_expenses()

    elif choice == "4":
        filter_by_category()

    elif choice == "5":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Try again.")
