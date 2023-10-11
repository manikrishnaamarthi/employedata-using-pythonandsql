import sqlite3

# Connect to the SQL database
conn = sqlite3.connect('employee_database.db')

# Create a cursor object
c = conn.cursor()

# Create the employee_working_table table
c.execute('''CREATE TABLE employee_working_table (
    employee_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    designation TEXT NOT NULL,
    department TEXT NOT NULL,
    start_date TEXT NOT NULL,
    end_date TEXT NULL
)''')

# Save the changes
conn.commit()

# Close the connection
conn.close()
