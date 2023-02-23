import mysql.connector
from mysql.connector import Error
# import pandas as pd


def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            # database=world,
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")
    return connection


# pw = input("Input password: ")
pw = "ghjhsd1989sql"
connection = create_server_connection("localhost", "root", pw)


def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print(f"Error: '{err}'")


# create_database_query = "CREATE DATABASE school"
# create_database(connection, create_database_query)


def execute_filename(connection, filename):
    # connection = create_server_connection("localhost", "root", pw)
    cursor = connection.cursor()
    try:
        fd = open(filename, 'r')
        sqlfile = fd.read()
        fd.close()
        # print(sqlfile)
        # cursor.execute(query)
        cursor.execute(sqlfile, multi=True)
        # connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")


def execute_query(connection, query):
    # connection = create_server_connection("localhost", "root", pw)
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        # cursor.execute(sqlfile, multi=True)
        # connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")


def read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: '{err}'")


# schema_query = "SOURCE D:\Android\Android Sync\!one-way to device - other\programming\Python\programs\exercises\!datasets\mysql_databases\sakila-db\sakila-schema.sql"
# data_query = "SOURCE D:\Android\Android Sync\!one-way to device - other\programming\Python\programs\exercises\!datasets\mysql_databases\sakila-db\sakila-data.sql"
execute_filename(connection, "world.sql")
connection = create_server_connection("localhost", "root", pw)
execute_query(connection, "use world")
# connection = create_server_connection("localhost", "root", pw)
# df = pd.read_sql_query("SELECT * from city", connection)
# df["newcol"] = "val"
# print(df)
