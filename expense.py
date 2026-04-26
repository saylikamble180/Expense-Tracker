def add_expense(conn,amount,category,date,description):
    cursor = conn.cursor()
    query = """INSERT INTO Expense (amount,category,date,description) VALUES (%s, %s, %s, %s)"""
    cursor.execute(query,(amount,category,date,description))
    conn.commit()

    print("Expense added successfully!")
    cursor.close()

def view_expenses(conn):
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Expense")
    results = cursor.fetchall()

    print("\n--- All Expenses ---")

    for row in results:
        print(row)

    cursor.close()

def get_total_expense(conn):
    cursor = conn.cursor
    cursor.execute("SELECT SUM(amount) FROM Expense")
    result = cursor.fetchone()[0]
    cursor.close()
    return result if result else 0

def category_summary(conn):
    cursor = conn.cursor()

    query = """
    SELECT category, SUM(amount)
    FROM Expense
    GROUP BY category
    """

    cursor.execute(query)
    results = cursor.fetchall()

    print("\n---Category Summary---")
    for row in results:
        print(row)

    cursor.close()

def monthly_summary(conn):
    cursor = conn.cursor()
    
    query = """
    SELECT MONTH (date), SUM(amount)
    FROM Expense
    GROUP BY MONTH(date)
    """

    cursor.execute(query)
    results = cursor.fetchall()

    print("\n---Monthly Summary---")

    months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]

    for row in results:
        month_name = months[row[0]-1]
        print(month_name,":",row[1])

    cursor.close()

def check_budget(conn,budget):
    cursor = conn.cursor()

    cursor.execute("SELECT SUM(amount) FROM Expense")
    total = cursor.fetchone()[0]
    total = total if total else 0

    print("\n---Budget Check---")
    print("Your Budget:",budget)
    print("Total Expense:", total)

    if total > budget:
        print("Warning: You are out of your budget!")
    else:
        print("You are within your budget.")

    cursor.close()