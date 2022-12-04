import mysql.connector

# connecting to the database using mysql connector 
try:

    example_db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "@rsenal8",
    database = "cafe_db"#---> how to connect to a database 
    

)
    
    print("connect to database")
except:
    print("failed to connect")

# cursor = example_db.cursor()                      

# try:
#     cursor.execute("Create DATABASE cafe_db")    ------> How to create a database 
#     print("Successful")

# except:
#     print("could not create database")

# cursor = example_db.cursor()

# product_menu_tb = '''CREATE TABLE IF NOT EXISTS products (
#     id INT PRIMARY KEY AUTO_INCREMENT NOT NULL, 
#     product_name TEXT NOT NULL, 
#     price FLOAT NOT NULL
# );'''

# get_products = '''SELECT * from products;''' # select query 

# try:
#     cursor.execute(product_menu_tb)
#     cursor.execute(get_products)
#     output = cursor.fetchall() # fetching all the data in the table 
#     for view in output:
#         print(view) # showing data in terminal 
#     print("successful in creating a table")
# except:
#     print("unsuccesful")

# finally:
#     cursor.close()
#     example_db.close()