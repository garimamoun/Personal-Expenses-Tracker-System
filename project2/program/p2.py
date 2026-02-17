import json
import os
from datetime import datetime

DATA_FILE = "expenses.json"

# -----------------------------
# Load Expenses from File
# -----------------------------
def load_expenses():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return []

# -----------------------------
# Save Expenses to File
# -----------------------------
def save_expenses(expenses):
    with open(DATA_FILE, "w") as file:
        json.dump(expenses, file, indent=4)

# -----------------------------
# Add Expense
# -----------------------------
def add_expense(expenses):
    date = input("Enter date (YYYY-MM-DD): ")
    description = input("Enter description: ")
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))

    expense = {
        "date": date,
        "description": description,
        "category": category,
        "amount": amount
    }

    expenses.append(expense)
    save_expenses(expenses)
    print("✅ Expense added successfully!")

# -----------------------------
# View Expenses
# -----------------------------
def view_expenses(expenses):
    if not expenses:
        print("⚠ No expenses found.")
        return

    for i, exp in enumerate(expenses):
        print(f"{i+1}. {exp['date']} | {exp['description']} | {exp['category']} | ₹{exp['amount']}")

# -----------------------------
# Delete Expense
# -----------------------------
def delete_expense(expenses):
    view_expenses(expenses)
    index = int(input("Enter expense number to delete: ")) - 1

    if 0 <= index < len(expenses):
        expenses.pop(index)
        save_expenses(expenses)
        print("🗑 Expense deleted successfully!")
    else:
        print("❌ Invalid selection!")

# -----------------------------
# Monthly Summary
# -----------------------------
def monthly_summary(expenses):
    month = input("Enter month (YYYY-MM): ")

    total = 0
    category_summary = {}

    for exp in expenses:
        if exp["date"].startswith(month):
            total += exp["amount"]
            category = exp["category"]

            if category in category_summary:
                category_summary[category] += exp["amount"]
            else:
                category_summary[category] = exp["amount"]

    print(f"\n📊 Summary for {month}")
    print(f"Total Expense: ₹{total}")

    print("\nCategory-wise Breakdown:")
    for cat, amt in category_summary.items():
        print(f"{cat}: ₹{amt}")

# -----------------------------
# Main Menu
# -----------------------------
def main():
    expenses = load_expenses()

    while True:
        print("\n==== PERSONAL EXPENSE TRACKER ====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Monthly Summary")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            delete_expense(expenses)
        elif choice == "4":
            monthly_summary(expenses)
        elif choice == "5":
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice!")

if __name__ == "__main__":
    main()
