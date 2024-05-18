import psycopg2
from config import host, user, password, db_name

connection = None

try:
    # connect to the database
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    connection.autocommit = True

    # the cursor for database operations
    with connection.cursor() as cursor:
        cursor.execute("SELECT version();")
        server_version = cursor.fetchone()
        print(f"Server version: {server_version}")

    # new table
    with connection.cursor() as cursor:
        cursor.execute(
            """CREATE TABLE users(
            id serial PRIMARY KEY,
            first_name varchar(50) NOT NULL,
            nick_name varchar(50) NOT NULL);"""
        )

        # connection.commit()
        print("[INFO] Table created successfully")

    # insert data
    with connection.cursor() as cursor:
        cursor.execute(
            """INSERT INTO users (first_name, nick_name) VALUES
            ('Oleg', 'barracuda');"""
        )

        print("[INFO] Data was succesfully inserted")

    # get data
    with connection.cursor() as cursor:
        cursor.execute(
            """SELECT nick_name FROM users WHERE first_name = 'Oleg';"""
        )

        print(cursor.fetchone())

except Exception as e:
    print("[INFO] Error while working with PostgreSQL:", e)
finally:
    if connection:
        connection.close()
        print("[INFO] PostgreSQL connection closed")
