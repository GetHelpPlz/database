import sqlite3

# Connect to the database
connection = sqlite3.connect('data.db')
cursor = connection.cursor()

# Create table (if it does not already exist)
cursor.execute("CREATE TABLE IF NOT EXISTS data (name TEXT, title TEXT, pay REAL)")

def get_name(cursor):
    cursor.execute("SELECT name FROM employees")
    results = cursor.fetchall()
    if len(results) == 0:
        print("No names in database")
        return None
    for i in range(len(results)):
        print(f"{i+1} - {results[i][0]}")
    choice = 0
    while choice < 1 or choice > len(results):
        choice = int(input("Name ID: "))
    return results[choice-1][0]


choice = None
while choice != "5":
    print("1) Display Namedata")
    print("2) Add User")
    print("3) Update User info")
    print("4) Delete User")
    print("5) Quit")
    choice = input("> ")
    print()
    if choice == "1":
        # Display Employees
        cursor.execute("SELECT * FROM employees ORDER BY pay DESC")
        print("{:>10}  {:>10}  {:>10}".format("Name", "Username", "Password"))
        for record in cursor.fetchall():
            print("{:>10}  {:>10}  {:>10}".format(record[0], record[1], record[2]))
    elif choice == "2":
        # Add New Employee
        try:
            name = input("Name: ")
            un = input("Username: ")
            pw = (input("Password: "))
            values = (name, un, pw)
            cursor.execute("INSERT INTO employees VALUES (?,?,?)", values)
            connection.commit()
        except ValueError:
            print("Invalid input!")
    elif choice == "3":
        # Update Employee Pay
        try:
            name = input("Name: ")
            password = input("New password: ")
            values = (password, name) # Make sure order is correct
            cursor.execute("UPDATE employees SET pay = ? WHERE name = ?", values)
            connection.commit()
            if cursor.rowcount == 0:
                print("Invalid name!")
        except ValueError:
            print("Invalid password!")
    elif choice == "4":
        # Delete employee
        name = get_name(cursor)
        if name == None:
            continue
        values = (name, )
        cursor.execute(" DELETE FROM employees WHERE name = ?", values)
        connection.commit()
    print()

# Close the database connection before exiting
connection.close()