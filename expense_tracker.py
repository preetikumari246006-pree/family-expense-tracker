import datetime
expenses = []
def add_expenses(amount, category, note):
  expense = {
    "amount": amount,
    "category": category,
    "note": note,
    "date": datetime.date.today()
  }
  
  expenses.append(expense)
  print("Expense added successfully!")

def view_expense():
  for expense in expenses:
    print("Amount   :", expense["amount"])
    print("Category :", expense["category"])
    print("Note     :", expense["note"])
    print("Date :", expense["date"])
    print("--------------------")

while True:
  choice = input("Enter the number between 1 to 3.")
  
  if choice == "1":
    amount = int(input("Enter your amount: "))
    category = input("Enter your category: ")
    note = input("Enter the short note: ")
    add_expenses(amount, category, note)
 
  elif choice == "2":
    view_expense()
  
  elif choice == "3":
    break
