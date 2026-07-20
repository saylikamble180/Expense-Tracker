CREATE DATABASE ExpenseTracker;
USE ExpenseTracker;

-- Income Table
CREATE TABLE Income (
    id INT AUTO_INCREMENT PRIMARY KEY,
    amount DECIMAL (10,2) NOT NULL,
    date DATE NOT NULL,
    source VARCHAR (50)
);

-- Expense Table
CREATE TABLE Expense (
    id INT AUTO_INCREMENT PRIMARY KEY,
    amount DECIMAL (10,2) NOT NULL,
    category VARCHAR(50),
    date DATE NOT NULL,
    description TEXT
);