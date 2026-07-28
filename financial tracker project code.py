

monthly_income = 0
total_expenses = 0
savings_goal = 0


expenses = []




print("Monthly Income:", monthly_income)
print("Total Expenses:", total_expenses)
print("Savings Goal:", savings_goal)
print("Expenses:", expenses)



for expense in expenses:
    print(expense)


print("\nExpenses above 500 ZMW:")
for expense in expenses:
    if expense["amount"] > 500:
        print(expense)



def add_expense(category, amount, date):
    expenses.append({"category": category, "amount": amount, "date": date})



def update_expense(category, new_amount):
    for expense in expenses:
        if expense["category"] == category:
            expense["amount"] = new_amount
            return
    print("Expense not found.")




def search_expenses(category):
    for expense in expenses:
        if expense["category"].lower() == category.lower():
            print(expense)



def adjust_expense(category, new_amount):
    if new_amount < 0:
        print("Amount cannot be negative")
        return
    update_expense(category, new_amount)



def check_budget(income, expenses):
    total = sum(exp["amount"] for exp in expenses)
    if total > income:
        print(" You are overspending!!!!")
    else:
        print("You are within budget.")



def calculate_balance(income, expenses):
    total_exp = sum(exp["amount"] for exp in expenses)
    balance = income - total_exp
    print("Total Income:", income)
    print("Total Expenses:", total_exp)
    print("Remaining Balance:", balance)
    return balance


def menu():
    
    global monthly_income
    
    while True:
        print("\n--- Personal Finance Tracker ---")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Update Expense")
        print("4. Display All Expenses")
        print("5. Search Expenses by Category")
        print("6. Adjust Expense")
        print("7. Check Budget")
        print("8. Calculate Balance")
        print("9. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            monthly_income += float(input("Enter income amount: "))
        elif choice == "2":
            category = input("Category: ")
            amount = float(input("Amount: "))
            date = input("Date (YYYY-MM-DD): ")
            add_expense(category, amount, date)
        elif choice == "3":
            category = input("Category to update: ")
            new_amount = float(input("New amount: "))
            update_expense(category, new_amount)
        elif choice == "4":
            for e in expenses:
                print(e)
        elif choice == "5":
            category = input("Category to search: ")
            search_expenses(category)
        elif choice == "6":
            category = input("Category: ")
            new_amount = float(input("New amount: "))
            adjust_expense(category, new_amount)
        elif choice == "7":
            check_budget(monthly_income, expenses)
        elif choice == "8":
            calculate_balance(monthly_income, expenses)
        elif choice == "9":
            print("Exiting program...")
            break
        else:
            print("Invalid choice!")


menu()

