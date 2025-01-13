import sqlite3

db_name: str = "HW_sql_3.db"
conn = sqlite3.connect(db_name) # creates a connector
conn.row_factory = sqlite3.Row # allow me to use column name

# cursor
cursor = conn.cursor()  # creates a cursor

cursor.execute("CREATE TABLE shopping (id INTEGER PRIMARY KEY, name TEXT, amount INTEGER);")

cursor.execute("INSERT INTO shopping VALUES (1, 'Avokado', 5);")
cursor.execute("INSERT INTO shopping VALUES (2, 'Milk', 2);")
cursor.execute("INSERT INTO shopping VALUES (3, 'Bread', 3);")
cursor.execute("INSERT INTO shopping VALUES (4, 'Chocolate', 8);")
cursor.execute("INSERT INTO shopping VALUES (5, 'Bamba', 5);")
cursor.execute("INSERT INTO shopping VALUES (6, 'Orange', 10);")

cursor.execute("SELECT * FROM shopping WHERE amount > 5")
cursor.execute("DELETE from shopping WHERE name like 'Orange';")
cursor.execute("UPDATE shopping SET name = 'Bisli' WHERE name LIKE 'Bamba'")
cursor.execute("UPDATE shopping SET amount=1 WHERE name LIKE 'Milk'")
cursor.execute("SELECT COUNT(*) from shopping")
cursor.execute("SELECT * FROM shopping WHERE id > 0")

conn.commit()
# cursor.execute("SELECT * FROM shopping")

rows = cursor.fetchall()
for row in rows:
    print(tuple(row))