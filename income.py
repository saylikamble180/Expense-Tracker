def add_income(conn, amount, date, source):
    cursor = conn.cursor()

    query = """
    INSERT INTO Income (amount, date, source)
    VALUES (%s, %s, %s)
    """

    cursor.execute(query, (amount, date, source))
    conn.commit()

    print("Income added successfully!")

    cursor.close()

def view_income(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Income")
    results = cursor.fetchall()

    print("\n---Income---")
    for row in results:
        print(row)

    cursor.close()

def get_total_income(conn):
    cursor = conn.cursor
    cursor.execute("SELECT SUM(amount) FROM Income")
    result = cursor.fetchone()[0]
    cursor.close()
    return result if result else 0