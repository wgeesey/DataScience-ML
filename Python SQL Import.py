# Create a database and then import dataset into the database using SQL Server
import pandas as pd
import pyodbc

# Step 1: Create a PD dataframe from the CSV.
csvpath = "C:\\Users\\willi\\Desktop\\DataScienceML\\Global Health Statistics.csv"
df = pd.read_csv(csvpath)

# Step 2: Define the SQL Server Connection to master (for creating the database)
conn = pyodbc.connect(''' 
    DRIVER={ODBC Driver 18 for SQL Server};
    SERVER=localhost\\SQLEXPRESS;
    DATABASE=master;
    Trusted_Connection=yes;
    Encrypt=yes;
    TrustServerCertificate=yes;
''', autocommit=True)  # 'autocommit=True' is a separate keyword, not part of the connection string.

# Step 3: Create the database if it doesn't exist, then USE it.
cursor = conn.cursor()  # Create a cursor object to execute SQL commands.

try:
    # Check if the database exists and create it if it doesn't.
    cursor.execute('''
        IF NOT EXISTS (
            SELECT name
            FROM sys.databases
            WHERE name = 'GlobalHealth')
        CREATE DATABASE GlobalHealth
    ''')
    print('GlobalHealth database has been created or already exists.')

    cursor.execute('USE GlobalHealth;')
    print('Switched to GlobalHealth database.')

    # Step 4: Create the table to hold the data from our csv.
    table_name = 'HealthStats'
    columns = []
    for column_name, dtype in df.dtypes.items():
        # Only wrap column names in brackets once
        if dtype == 'object':
            columns.append(f'[{column_name}] NVARCHAR(100)')
        elif dtype == 'int64':
            columns.append(f'[{column_name}] INT')
        elif dtype == 'float64':
            columns.append(f'[{column_name}] FLOAT')
        elif dtype == 'bool':
            columns.append(f'[{column_name}] BIT')
        else:
            # Ensure NVARCHAR is properly closed with a parenthesis
            columns.append(f'[{column_name}] NVARCHAR(100)')

    # Join columns into a string for the SQL query
    columns_str = ", ".join(columns)

    # Create the table if it doesn't exist
    cursor.execute(f'''
        IF NOT EXISTS (
            SELECT * 
            FROM sys.tables
            WHERE name = '{table_name}')
        BEGIN
            CREATE TABLE {table_name} ({columns_str})
        END''')
    print(f'Table {table_name} created or already exists.')

    # Step 5: Insert the data from the csv into the table.
    for i, row in df.iterrows():
        # Format column names with brackets
        column_names = ', '.join([f'[{col}]' for col in df.columns])

        # Use placeholders for values
        placeholders = ', '.join(['?' for _ in df.columns])

        # Construct the SQL INSERT query dynamically
        query = f'''
            INSERT INTO {table_name} ({column_names}) 
            VALUES ({placeholders})
        '''

        # Execute the query with the values as a tuple
        cursor.execute(query, tuple(row))
        
except Exception as e:
    print(f'Exception occurred: {e}')

# Close the connection
conn.close()
