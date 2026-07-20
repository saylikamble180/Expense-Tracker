# 💰 Smart Expense Tracker
 
A console-based expense tracker built using Python and MySQL to manage income, track expenses, analyze spending patterns, and monitor overall financial balance.

---

## Features

### Income Management
- Add income with amount, date, and source (e.g., salary, freelance)
- View all recorded income entries

### Expense Tracking
- Add expenses with category, date, and description
- Store and manage all expense records in the database

### Category-wise Analysis
- View total spending for each category (e.g., Food, Travel)
- Helps identify where most money is being spent

### Monthly Analysis
- Displays total expenses month-wise
- Helps track spending trends over time

### Balance Calculation
- Calculates total income and total expenses
- Displays remaining balance

### Budget Alert System
- Allows user to set a budget
- Warns when total expenses exceed the budget

### Data Viewing
- View all income and expense records in a structured format

---

## Project Structure
```
expense-tracker/
│
├── main.py          # Main program (menu and user interaction)
├── connect.py       # Database connection setup
├── expense.py       # Expense-related functions
├── income.py        # Income-related functions
├── Schema_ET.sql    # SQL script to create database and tables
├── README.md        # Project documentation
└── .gitignore       # Ignored files and folders
```

The project is structured in a modular way, separating database connection, business logic, and user interaction for better readability and maintainability.

---

## Tech Stack

- Python
- MySQL
- mysql-connector-python

---

## Database Design
Full schema available in `Schema_ET.sql`.

### Income Table

- "id" (Primary Key)
- "amount"
- "income_date"
- "source"

### Expense Table

- "id" (Primary Key)
- "amount"
- "category"
- "expense_date"
- "description"
  
---

## Sample Output
```
===== Expense Tracker =====
1. Add Income
2. Add Expense
3. View Expenses
4. View Income
5. Show Balance
6. Category Summary
7. Monthly Summary
8. Check Budget
9. Exit

Enter your choice: 5

--- Summary ---
Total Income: 7000
Total Expense: 2500
Balance: 4500
```
---

## How to Run

1. Set your MySQL password as an environment variable:
   
   setx DB_PASSWORD "your_password"

2. Run the program:
   
   python main.py

---

## Future Improvements

- Update and delete functionality (CRUD completion)
- Data visualization (charts)

---

## Key Learnings

- Connecting Python with MySQL
- Writing SQL queries (INSERT, SELECT, SUM, GROUP BY)
- Structuring a modular Python project
- Implementing real-world logic (budget tracking & analytics)
- Learned to use Git and Github for version control

---

## 👩‍💻 Author

Sayli Kamble
