import mysql.connector

def get_connection():
    connection = mysql.connector.connect(host='swastha.clcyg6mwkr6z.ap-south-1.rds.amazonaws.com',
                                         database='kkkr',
                                         user='admin',
                                         password='Vts2022apr')
    return connection

def close_connection(connection):
    if connection:
        connection.close()