expenses = []
def add_expenses(amount, category, note):
  expense = {
    "amount": amount,
    "category": category,
    "note": note
  }

  expenses.append(expense)
  print("Expense added successfully!")

def view_expense():
  for i in expenses:
    print(i)

add_expenses(400, "food", "breakfast")
view_expense()
