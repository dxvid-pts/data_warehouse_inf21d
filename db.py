import os
import psycopg2
import json

def create_table_if_not_exist():
    try:
        password = os.environ.get('PG_PASSWORD')
        # Replace with your database credentials
        conn = psycopg2.connect(
            database="dhbw", 
            user="postgres", 
            host="localhost", 
            port="5432" 
        )

        cursor = conn.cursor()

         # Create schema "staging" if not exists
        create_schema_query = """
            CREATE SCHEMA IF NOT EXISTS staging;
        """

        cursor.execute(create_schema_query)
        conn.commit()

        # Create table "messung" if not exists
        create_table_query = """
            CREATE TABLE IF NOT EXISTS staging.messung (
                messung_id SERIAL PRIMARY KEY,
                payload JSON NOT NULL,
                empfangen TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
            );
        """

        cursor.execute(create_table_query)
        conn.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn:
            cursor.close()
            conn.close()
            print("PostgreSQL connection closed")
   
