import mysql.connector

def get_connection():
    connection = mysql.connector.connect(host='localhost',
                                         database='kkkr',
                                         user='root',
                                         password='Ashrith@26')
    return connection

def close_connection(connection):
    if connection:
        connection.close()