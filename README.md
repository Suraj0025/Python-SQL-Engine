# 🛠️ Python-SQL-Engine

This project builds a lightweight SQL execution engine using Python and MySQL Connector, allowing you to simulate basic database operations (DDL + DML) directly via Python functions. It’s an end-to-end database interaction project — from creating a database to running queries like `SELECT`, `WHERE`, `ORDER BY`, `UPDATE`, and `DELETE`.

Perfect for those learning database programming, SQL query logic, or how Python interacts with relational databases.

---

## 💡 Features

- ✅ Create and connect to MySQL databases
- ✅ Execute raw SQL queries via Python
- ✅ Perform CRUD operations (`CREATE`, `INSERT`, `SELECT`, `UPDATE`, `DELETE`)
- ✅ Display query results using Pandas DataFrames
- ✅ Supports advanced SQL features like `DISTINCT`, `ORDER BY`, `BETWEEN`, etc.

---

## 🧱 Technologies Used

- **Python 3.x**
- **MySQL Connector (`mysql-connector-python`)**
- **MySQL Server**
- **Pandas (for tabular output)**

---

## 🚀 Getting Started

### 1. Install Requirements

```bash
pip install mysql-connector-python pandas
````

### 2. MySQL Setup

Make sure your MySQL server is running and you have a root password. Update this in the code:

```python
pw = "YourMySQLPasswordHere"
```

---

## 📁 Project Overview

```
Python-SQL-Engine/
├── main.py           
├── requirements.txt  
└── README.md         
```

---

## 🔍 Key Code Highlights

```python
# Create database connection
def create_server_connection(host_name, user_name, user_passwd):
    connection = mysql.connector.connect(
        host=host_name, user=user_name, passwd=user_passwd
    )
    return connection

# Create and run SQL queries
def execute_query(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
```

Example Queries You Can Run:

```sql
SELECT * FROM orders;
SELECT customer_name, phone_number FROM orders;
SELECT DISTINCT YEAR(date_ordered) FROM orders;
SELECT * FROM orders ORDER BY unit_price DESC;
```

---

## 📊 Output Format

Using Pandas to format final query results into a readable table:

```python
df = pd.DataFrame(from_db, columns=columns)
print(df)

## 📜 License

This project is licensed under the [MIT License](LICENSE).

## 🙋‍♂️ Author

Made by **[Suraj Mahadik](https://www.linkedin.com/in/suraj-mahadik-341b91315/)**
Feel free to connect or drop feedback!

### ✅ Suggestions to Complete the Repo:

- Save your code as `main.py`  
- (Optional) Add a `requirements.txt`:
```

mysql-connector-python
pandas

````
- Fix minor typo in:
```python
dalete → delete
roots → root (in db connection)
