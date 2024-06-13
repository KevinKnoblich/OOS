# rudimentary automated data generation on a schedule
# needs to be converted to cron job once project migrates onto unix

import sqlite3
from faker import Faker
import schedule
import time

fake = Faker()
conn = sqlite3.connect('oos.db')
cursor = conn.cursor()

# generate new sales data directly to db
def generate_sales_data():
    # Generate fake sales data
    new_sales = {
        'date': fake.date(),
        'customer_id': fake.random_int(min=1, max=100),
        'product_id': fake.random_int(min=1, max=100),
        'amount': fake.random_int(min=1, max=1000)
    }
    insert_data('sales', tuple(new_sales.values()))


# schedule task
schedule.every().day.at("10:00").do(generate_sales_data)


# insert data into table
def insert_data(table, data):
    placeholders = ', '.join(['?'] * len(data))
    sql = f'INSERT INTO {table} VALUES ({placeholders})'
    cursor.execute(sql, data)
    conn.commit()

# run scheduler
while True:
    schedule.run_pending()
    time.sleep(1)
