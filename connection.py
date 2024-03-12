import mysql.connector
from os import environ
def get_connection():
    connection = mysql.connector.connect(host=environ.get('HOST'),
                                         database=environ.get('DB'),
                                         user=environ.get('USER'),
                                         password=environ.get('PASSWORD'),
                                         port=environ.get('PORT'))
    return connection

def close_connection(connection):
    if connection:
        connection.close()