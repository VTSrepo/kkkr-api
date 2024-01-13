import mysql.connector
import requests
from connection import get_connection,close_connection


def get_profiles():
    try:
        connection = get_connection()
        cursor = connection.cursor()
        sql_select_query = """select * from profile_master"""
        cursor.execute(sql_select_query)
        records = cursor.fetchall()
        print("Printing org details", "\n")
        
        print()
        for row in records:
            x = {"profile_name":row[0], "profile_code":row[1]}
            print(x);
            # print("Org Id: ", row[0])
            # print("Org Name:", row[1])            
        close_connection(connection)
        return x;        
    except (Exception, mysql.connector.Error) as error:
        print("Error while getting data", error)
