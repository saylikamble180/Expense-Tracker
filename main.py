from connect import get_connection
from expense import add_expense, view_expenses,get_total_expense,category_summary,monthly_summary,check_budget
from income import add_income,view_income,get_total_income

conn = get_connection("ExpenseTracker")

while True:
    print("\n=== Expense Tracker ===")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Add Income")
    print("4. View Income")
    print("5. Show Balance")
    print("6. Category Summary")
    print("7. Monthly Summary")
    print("8. Check Budget")
    print("9. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        amount = float(input("Enter amount: "))
        category = input("Enter category: ")
        date = input("Enter date (YYYY-MM-DD): ")
        description = input("Enter description: ")

        add_expense(conn, amount, category, date, description)

    elif choice == "2":
        view_expenses(conn)

    elif choice == "3":
        amount = float(input("Enter amount: "))
        date = input("Enter date (YYYY-MM-DD): ")
        source = input("Enter source: ")

        add_income(conn, amount, date, source)

    elif choice == "4":
        view_income(conn)

    elif choice == "5":
        income = get_total_income(conn)
        expense = get_total_expense(conn)
        print("\n---Sammary---")
        print("Total Income:",income)
        print("Total Expense:",expense)
        print("Balance:",income-expense)

    elif choice == "6":
        category_summary(conn)

    elif choice == "7":
        monthly_summary(conn)

    elif choice == "8":
        budget = float(input("Enter your budget:"))
        check_budget(conn,budget)

    elif choice == "9":
        print("Exiting...")
        break

    else:
        print("Invalid choice")

conn.close()