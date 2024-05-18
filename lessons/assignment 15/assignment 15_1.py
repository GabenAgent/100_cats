import psycopg2
from config import host, user, password, db_name

connection = psycopg2.connect(
    host=host,
    user=user,
    password=password,
    database=db_name
)

create_users_table = """
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);
"""

create_hosts_table = """
CREATE TABLE hosts (
    host_id SERIAL PRIMARY KEY,
    user_id INTEGER UNIQUE NOT NULL REFERENCES users(user_id)
);
"""

create_rooms_table = """
CREATE TABLE rooms (
    room_id SERIAL PRIMARY KEY,
    host_id INTEGER NOT NULL REFERENCES hosts(host_id),
    title VARCHAR(100) NOT NULL,
    description TEXT NOT NULL,
    residents INTEGER NOT NULL,
    price NUMERIC(10, 2) NOT NULL,
    ac BOOLEAN NOT NULL,
    refrigerator BOOLEAN NOT NULL
);
"""

create_reservations_table = """
CREATE TABLE reservations (
    reservation_id SERIAL PRIMARY KEY,
    room_id INTEGER NOT NULL REFERENCES rooms(room_id),
    guest_id INTEGER NOT NULL REFERENCES users(user_id),
    check_in DATE NOT NULL,
    check_out DATE NOT NULL
);
"""

create_reviews_table = """
CREATE TABLE reviews (
    review_id SERIAL PRIMARY KEY,
    room_id INTEGER NOT NULL REFERENCES rooms(room_id),
    guest_id INTEGER NOT NULL REFERENCES users(user_id),
    rating INTEGER CHECK (rating >= 1 AND rating <= 5) NOT NULL,
    comment TEXT
);
"""

try:
    cur = connection.cursor()

    cur.execute(create_users_table)
    cur.execute(create_hosts_table)
    cur.execute(create_rooms_table)
    cur.execute(create_reservations_table)
    cur.execute(create_reviews_table)

    connection.commit()
    print("Tables are done!!!")
except Exception as e:
    print("[INFO] Error while working with PostgreSQL:", e)
finally:
    if connection:
        connection.close()
        print("[INFO] PostgreSQL connection closed")
