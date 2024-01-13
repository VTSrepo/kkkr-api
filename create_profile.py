import requests
from connection import get_connection,close_connection

def create_profile():
    try:
        connection = get_connection()
        cursor = connection.cursor()
        sql = """insert into profile_master (profile_source,
        profile_code, 
        profile_name,  
        gendar  ,
        profile_type,  
        dob ,
        age ,
        caste_sect,  
        subsect  ,
        add_subsect, 
        gothram  ,
        star_paadam,  
        rasi  ,
        birth_time,  
        birth_place, 
        education  ,
        occupation  ,
        annual_income, 
        job_location  ,
        height  ,
        weight  ,
        father_detail,  
        mother_detail , 
        sibling_detail , 
        contact_relation,  
        primary_contact ,
        secondary_contact,  
        email_id  ,
        brief_detail , 
        expectation  ,
        other_info  ,
        agree_inform_marriage,  
        agree_inform_exit  ,
        self_declaration  ,
        created_by  ,
        created_date , 
        updated_by  ,
        updated_date , 
        star )  values 
        (  ) VALUES (%s, %s)"""
        val = ("John", "Highway 21")
        cursor.execute(sql, val)
        # sql_select_query = """select * from profile_master"""
        # cursor.execute(sql_select_query)
        
        connection.commit();
        print(cursor.rowcount, "record inserted.")          
        close_connection(connection)
        return x;        
    except (Exception, mysql.connector.Error) as error:
        print("Error while inserting data", error)