"""Helper functions to interact with the database."""

import json
import os

import psycopg2


def connect_to_db():
    """
    Creates a connection to the database and returns the connection and cursor.
    """
    try:
        password = os.environ.get("PG_PASSWORD")
        conn = psycopg2.connect(
            database="dhbw",
            user="postgres",
            password=password,
            host="localhost",
            port="5432",
        )
        cursor = conn.cursor()
        return conn, cursor
    except psycopg2.DatabaseError as error:
        print(error)
        return None, None


def create_table_if_not_exist():
    """
    Creates a schema and table if they do not exist.
    """
    conn, cursor = connect_to_db()
    if conn is not None and cursor is not None:
        try:
            # Create schema "staging" if not exists
            create_schema_query = """
                CREATE SCHEMA IF NOT EXISTS staging;
            """
            cursor.execute(create_schema_query)

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
        except psycopg2.DatabaseError as error:
            print(error)
        finally:
            cursor.close()
            conn.close()


def write_row(payload):
    """
    Inserts a new row into the staging.messung table with the given payload.
    """
    conn, cursor = connect_to_db()
    if conn is not None and cursor is not None:
        try:
            insert_query = """
                INSERT INTO staging.messung (payload) VALUES (%s);
            """
            cursor.execute(insert_query, (json.dumps(payload),))
            conn.commit()
        except psycopg2.DatabaseError as error:
            print(error)
        finally:
            cursor.close()
            conn.close()
