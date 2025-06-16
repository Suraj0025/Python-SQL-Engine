import mysql.connector
from mysql.connector import Error
import pandas as pd

def create_server_connection(host_name, user_name, user_passwd):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = host_name,
            user = user_name,
            passwd = user_passwd
            )
        print("MySQL Database connectiion successful")
    except Error as err:
        print(f"Error: '{err}'")
    return connection

#put our mysql terminal password
pw = "Suraj@1234"

#Database name
db = "mysql_python"
connection = create_server_connection("localhost", "root", pw)

#Create mysql_python
def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print(f"Error: '{err}'")
create_database_query = "CREATE DATABASE mysql_python"
create_database(connection, create_database_query)

#Connect to the database

def create_db_connection(host_name, user_name, user_passwd, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = host_name,
            user = user_name,
            passwd = user_passwd,
            database= db_name)
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")
    return connection

#Execute sql queries
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as err:
        print(f"Error: '{err}'")

#Create a table
create_orders_table = """
create table orders(
order_id int primary key,
customer_name varchar(30) not null,
product_name varchar(20) not null,
date_ordered date ,
quantity int,
unit_price float,
pnone_number varchar(20));
"""
#connect to the database
connection = create_db_connection("localhost", "root", pw, db)
execute_query(connection, create_orders_table)

#Insert data into the table
data_orders = """
insert into orders values
(101, 'John Doe', 'Laptop', '2021-01-01', 1, 50000, '1234567890'),
(102, 'Jane Doe', 'Mobile Phone', '2021-01-02', 2, 20000, '0987654321'),
(103, 'John Smith', 'Tablet', '2021-01-03', 1, 30000, '1234509876'),
(104, 'Jane Smith', 'Desktop', '2021-01-04', 1, 60000, '0987612345'),
(105, 'John Doe', 'Smart Watch', '2021-01-05', 1, 10000, '1234598760');
"""
connection  = create_db_connection("localhost", "roots", pw, db)
execute_query(connection, data_orders)

#Select data from the table
def read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: '{err}'")

#Using select satatement
Q1 = """
select * from orders;
"""
connection = create_db_connection("localhost", "roots", pw, db)
results = read_query(connection, Q1)
for result in results:
    print(result)

Q2 = """
select customer_name, phone_number from orders;
"""
connection = create_db_connection("localhost", "roots", pw, db)
results = read_query(connection, Q2)
for result in results:
    print(result)

Q3 = """
select year(date_ordered) as year from orders;
"""
connection = create_db_connection("localhost", "roots", pw, db)
results = read_query(connection, Q3)
for result in results:
    print(result)

Q4 = """
select distinct year(date_ordered) from orders;
"""
connection = create_db_connection("localhost", "roots", pw, db)
results = read_query(connection, Q4)
for result in results:
    print(result)

Q5 = """
select * from orders where date_ordered between '2021-01-01' and '2021-01-03';
"""
connection = create_db_connection("localhost", "roots", pw, db)
results = read_query(connection, Q5)
for result in results:
    print(result)

Q6 = """
select *from orders order by unit_price desc;
"""
connection = create_db_connection("localhost", "roots", pw, db)
results = read_query(connection, Q6)
for result in results:
    print(result)

from_db = []
for result in results:
    result = list(result)
    from_db.append(result)
columns = ["order_id", "customer_name", "product_name", "date_ordered", "quantity", "unit_price", "phone_number"]
df = pd.DataFrame(from_db, columns = columns)

print(df)

#Update data in the table
update = """
update orders
set unit_price = 70000
where order_id = 104;
"""
connection = create_db_connection("localhost", "roots", pw, db)
execute_query(connection, update)

#Delete data from the table
delete_order = """
dalete from orders
where order_id = 105;
"""
connection = create_db_connection("localhost", "roots", pw, db)
execute_query(connection, delete_order)

Q7 = """
select *from orders;
"""
connection = create_db_connection("localhost", "roots", pw, db)
results = read_query(connection, Q7)
for result in results:
    print(result)



