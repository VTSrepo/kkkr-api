import mysql.connector
import requests

def get_connection():
    connection = mysql.connector.connect(host='localhost',
                                         database='kkkr',
                                         user='root',
                                         password='Ashrith@26')
    return connection

def close_connection(connection):
    if connection:
        connection.close()

def get_org_details():
    try:
        connection = get_connection()
        cursor = connection.cursor()
        sql_select_query = """select * from org_master"""
        cursor.execute(sql_select_query)
        records = cursor.fetchall()
        print("Printing org details", "\n")
        
        print()
        for row in records:
            x = {"OrgId":row[0], "OrgName":row[1]}
            print(x);
            print("Org Id: ", row[0])
            print("Org Name:", row[1])            
        close_connection(connection)
        return x;        
    except (Exception, mysql.connector.Error) as error:
        print("Error while getting data", error)