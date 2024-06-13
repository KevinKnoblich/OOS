### NOT FUNCTIONAL UNTIL DATABASE GENERATES DATA CONTAINING INSIGHTS

import pandas as pd
import sqlite3
import matplotlib.pyplot as plt


conn = sqlite3.connect('oos.db')

# load data into pandas
employees_df = pd.read_sql_query('SELECT * FROM employees', conn)
customers_df = pd.read_sql_query('SELECT * FROM customers', conn)
products_df = pd.read_sql_query('SELECT * FROM products', conn)

print(employees_df.describe())

# sales trends NEED TO IMPLEMENT SALES
# sales_trends = sales_df.groupby('date')['amount'].sum()
# sales_trends.plot(kind='line')
# plt.title('Sales Trends')
# plt.xlabel('Date')
# plt.ylabel('Sales Amount')
# plt.show()

# customer demographics NEED TO OVERHAUL CUSTOMER DATA GENERATION TO INCLUDE AGE AND COUNTRY
# customer_demographics = customers_df['age'].value_counts()
# customer_demographics.plot(kind='bar')
# plt.title('Customer Age Demographics')
# plt.xlabel('Age')
# plt.ylabel('Count')
# plt.show()

# Close the database connection
conn.close()
