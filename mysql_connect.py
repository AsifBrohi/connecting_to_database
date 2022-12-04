import mysql.connector

# connecting to the database using mysql connector
try:

    db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "@rsenal8",
    database = "flight_distance"


)

    print("connect to database")
except:
    print("failed to connect")





cursor = db.cursor()

# #creating a database

# try:
#     cursor.execute('''Create DATABASE flight_distance
#     ''')
#     print("Database created")
# except:
#     print("Database not created")




#create a table in database

flight = '''Create Table if not exists flights(
    path_id int primary key auto_increment not null,
    normalised_city_pair varchar(200) not null,
    departure_code varchar(200) not null,
    arrival_Code varchar(200) not null,
    distance_miles int not null,
    distance_Km int not null
);
'''

cursor.execute(flight) # created table in

show_tables = '''Show tables;'''
cursor.execute(show_tables)
result = cursor.fetchall()
for x in result:
    print(x)

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