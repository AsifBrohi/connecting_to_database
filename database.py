# creating database with sqlite3 

import sqlite3
#creating a database / connecting to it 
conn = sqlite3.connect('/Users/AsifB/Documents/Data_engineering_new_gen/connecting_database_python/example.db')

# creating a table in database using execute 
try:

    conn.execute('''
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
    product_name TEXT NOT NULL, 
    price FLOAT NOT NULL
);''')
    print("successful")
except:
    print("unsuccessful")


conn.commit() # committing changes ?
conn.close() # closing connection 


