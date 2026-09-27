import sqlite3

print("==============================")
print("      EXPENSE ANALYTICS")
print("==============================")

# Connect to database
connection = sqlite3.connect("expenses.db")

# Create cursor
cursor = connection.cursor()

print("Database connected successfully!")

# Create expenses table
cursor.execute("""
CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    description TEXT NOT NULL,
    amount REAL NOT NULL,
    category TEXT NOT NULL
)
""")

connection.commit()

print("Expenses table created successfully!")
def add_expense():
    print()
    print("----- Add Expense -----")

    description = input("Enter expense description: ")
    amount = float(input("Enter expense amount: "))
    category = input("Enter expense category: ")

    cursor.execute(
        """
        INSERT INTO expenses (description, amount, category)
        VALUES (?, ?, ?)
        """,
        (description, amount, category)
    )

    connection.commit()

    print("Expense added successfully!")

# Main menu
while True:

    print()
    print("========== EXPENSE ANALYTICS ==========")
    print("1. Add Expense")
    print("2. View Total Expense")
    print("3. View Average Expense")
    print("4. View Category-wise Expenses")
    print("5. Exit")
    print("=======================================")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        cursor.execute("SELECT SUM(amount) FROM expenses")
        total_expense = cursor.fetchone()[0]

        if total_expense is None:
            total_expense = 0

        print("Total Expenses: ₹", total_expense)

    elif choice == "3":
        cursor.execute("SELECT AVG(amount) FROM expenses")
        average_expense = cursor.fetchone()[0]

        if average_expense is None:
            average_expense = 0

        print("Average Expense: ₹", round(average_expense, 2))

    elif choice == "4":
        cursor.execute("""
        SELECT category, SUM(amount)
        FROM expenses
        GROUP BY category
        """)

        category_expenses = cursor.fetchall()

        print()
        print("----- Category-wise Expenses -----")

        for category, total in category_expenses:
            print(category, ": ₹", total)

    elif choice == "5":
        print("Thank you for using Expense Analytics!")
        break

    else:
        print("Invalid choice. Please try again.")

connection.close()