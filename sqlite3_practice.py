import sqlite3
import sys

import pandas as pd

filename = "D:\\Android\\Android Sync\\!one-way to device - other\\programming\\Python\\programs\\exercises\\!datasets\\sakila-data.sql"
try:
    conn = sqlite3.connect('database.db')
except Error as e:
    print(e)
# conn.close()
#  Create a cursor to allow to execute SQL commands
cursor = conn.cursor()
#  Create a SQL Table
sql_command = '''
    CREATE TABLE IF NOT EXISTS contacts (
        Id INTEGER PRIMARY KEY AUTOINCREMENT,
        Firstname TEXT,
        Lastname TEXT,
        Email TEXT
    )'''

cursor.execute(sql_command)

#  Commit the changes to the database
conn.commit()

insert_data = """
    INSERT INTO contacts
    (Firstname, Lastname, Email)
    VALUES (
        'David',
        'Attenborough',
        'dattenborough@example.com'
    )
"""
cursor.execute(insert_data)

#  Commit the changes to the database
conn.commit()

df = pd.read_sql_query("SELECT * from contacts", conn)
df["newcol"] = "val"
print(df)
df.to_sql("df", conn, if_exists="replace")
