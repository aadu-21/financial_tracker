import os

EXPENSE_FILE = "expenses.txt"

def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category: ")
    amount = input("Enter amount: ")
    description = input("Enter description (optional): ")

    with open(EXPENSE_FILE, "a") as file:
        file.write(f"{date},{category},{amount},{description}\n")

    print("Expense added successfully!\n")

def view_expenses():
    if not os.path.exists(EXPENSE_FILE):
        print("No expenses recorded yet.\n")
        return

    print("\nRecorded Expenses:")
    with open(EXPENSE_FILE, "r") as file:
        for line in file:
            date, category, amount, description = line.strip().split(",")
            print(f"Date: {date}, Category: {category}, Amount: {amount}, Description: {description}")

    print()

def delete_expense():
    if not os.path.exists(EXPENSE_FILE):
        print("No expenses recorded yet.\n")
        return

    expenses = []
    with open(EXPENSE_FILE, "r") as file:
        expenses = file.readlines()

    for i, line in enumerate(expenses, 1):
        print(f"{i}. {line.strip()}")

    try:
        choice = int(input("Enter the expense number to delete: "))
        if 1 <= choice <= len(expenses):
            del expenses[choice - 1]
            with open(EXPENSE_FILE, "w") as file:
                file.writelines(expenses)
            print("Expense deleted successfully!\n")
        else:
            print("Invalid selection.\n")
    except ValueError:
        print("Invalid input. Please enter a number.\n")

def show_total():
    if not os.path.exists(EXPENSE_FILE):
        print("No expenses recorded yet.\n")
        return

    total = 0
    with open(EXPENSE_FILE, "r") as file:
        for line in file:
            _, _, amount, _ = line.strip().split(",")
            total += float(amount)

    print(f"Total Expenses: Rs.{total:.2f}\n")

SAVINGS_FILE = "savings.txt"

def add_savings():
    date = input("Enter date (YYYY-MM-DD): ")
    amount = input("Enter savings amount: ")
    description = input("Enter description (optional): ")

    with open(SAVINGS_FILE, "a") as file:
        file.write(f"{date},{amount},{description}\n")

    print("Savings recorded successfully!\n")

def view_savings():
    if not os.path.exists(SAVINGS_FILE):
        print("No savings recorded yet.\n")
        return

    print("\nSavings History:")
    with open(SAVINGS_FILE, "r") as file:
        for line in file:
            date, amount, description = line.strip().split(",")
            print(f"Date: {date}, Amount: {amount}, Description: {description}")

    print()

def delete_savings():
    if not os.path.exists(SAVINGS_FILE):
        print("No savings recorded yet.\n")
        return

    savings = []
    with open(SAVINGS_FILE, "r") as file:
        savings = file.readlines()

    for i, line in enumerate(savings, 1):
        print(f"{i}. {line.strip()}")

    try:
        choice = int(input("Enter the savings number to delete: "))
        if 1 <= choice <= len(savings):
            del savings[choice - 1]
            with open(SAVINGS_FILE, "w") as file:
                file.writelines(savings)
            print("Savings entry deleted successfully!\n")
        else:
            print("Invalid selection.\n")
    except ValueError:
        print("Invalid input. Please enter a number.\n")

def show_savings_balance():
    if not os.path.exists(SAVINGS_FILE):
        print("No savings recorded yet.\n")
        return

    total = 0
    with open(SAVINGS_FILE, "r") as file:
        for line in file:
            _, amount, _ = line.strip().split(",")
            total += float(amount)

    print(f"Total Savings: Rs.{total:.2f}\n")



def main():
    while True:
        print("\nExpense & Savings Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Show Total Expenses")
        print("5. Add Savings")
        print("6. View Savings")
        print("7. Delete Savings")
        print("8. Show Total Savings")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            delete_expense()
        elif choice == "4":
            show_total()
        elif choice == "5":
            add_savings()
        elif choice == "6":
            view_savings()
        elif choice == "7":
            delete_savings()
        elif choice == "8":
            show_savings_balance()
        elif choice == "9":
            print("Exiting... Have a great day!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 9.\n")

if __name__ == "__main__":
    main()
