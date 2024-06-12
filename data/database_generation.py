import pandas as pd
import sqlite3

# infer SQL type from pandas dtype
def infer_sql_type(dtype):
    if pd.api.types.is_integer_dtype(dtype):
        return "INTEGER"
    elif pd.api.types.is_float_dtype(dtype):
        return "REAL"
    elif pd.api.types.is_bool_dtype(dtype):
        return "BOOLEAN"
    else:
        return "TEXT"

# create a table from CSV header
def create_table_from_csv(conn, table_name, csv_file):
    df = pd.read_csv(csv_file)
    columns = df.columns
    dtypes = df.dtypes

    columns_with_types = [f'"{col}" {infer_sql_type(dtype)}' for col, dtype in zip(columns, dtypes)]
    columns_with_types_str = ", ".join(columns_with_types)

    create_table_sql = f'CREATE TABLE IF NOT EXISTS {table_name} ({columns_with_types_str});'
    cursor = conn.cursor()
    cursor.execute(create_table_sql)
    conn.commit()


# import CSV data into SQLite table
def import_csv_to_sqlite(conn, table_name, csv_file):
    df = pd.read_csv(csv_file)
    df.to_sql(table_name, conn, if_exists='replace', index=False)


# database name goes here (will create if not existent)
db_name = 'oos.db'
conn = sqlite3.connect(db_name)

# file names go here
csv_files = {
    'employees': 'employees.csv',
    'customers': 'customers.csv',
    'products': 'products.csv',
}

for table_name, csv_file in csv_files.items():
    create_table_from_csv(conn, table_name, csv_file)
    import_csv_to_sqlite(conn, table_name, csv_file)

# Close db conn
conn.close()

print("Database created and data imported successfully!")
