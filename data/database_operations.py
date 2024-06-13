import sqlite3

conn = sqlite3.connect('oos.db')
cursor = conn.cursor()

# if you want to run this in command line
# print("Connected to oos.db successfully")


# insert data into table
def insert_data(table, data):
    placeholders = ', '.join(['?'] * len(data))
    sql = f'INSERT INTO {table} VALUES ({placeholders})'
    cursor.execute(sql, data)
    conn.commit()


# fetch data from table
def fetch_data(table):
    cursor.execute(f'SELECT * FROM {table}')
    rows = cursor.fetchall()
    return rows

# fetch all employees
# employees = fetch_data('employees')
# for emp in employees:
#     print(emp)


# Function to update data in a table
def update_data(table, column, new_value, condition):
    sql = f'UPDATE {table} SET {column} = ? WHERE {condition}'
    cursor.execute(sql, (new_value,))
    conn.commit()


# delete data from table
def delete_data(table, condition):
    sql = f'DELETE FROM {table} WHERE {condition}'
    cursor.execute(sql)
    conn.commit()

# delete an employee
# delete_data('employees', 'id = 1337')

# Close database connection
conn.close()
# print("Database connection closed")

