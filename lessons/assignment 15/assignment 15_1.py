import psycopg2
from config import host, user, password, db_name

connection = psycopg2.connect(
    host=host,
    user=user,
    password=password,
    database=db_name
)


def create_tables_and_insert_data():

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

    insert_users = """
    INSERT INTO users (username, password, email) VALUES 
    ('Bob', 'qwerty', 'bob@ukr.com'),
    ('Jane', '12345', 'jane@gmail.com'),
    ('Max', 'qwerty123', 'max@bigmir.net');
    """

    insert_hosts = """
    INSERT INTO hosts (user_id) VALUES 
    (1), 
    (2), 
    (3);
    """

    insert_rooms = """
    INSERT INTO rooms (host_id, title, description, residents, price, ac, refrigerator) VALUES 
    (1, 'Cozy Cottage', 'A small, cozy cottage in the countryside.', 4, 150.00, TRUE, TRUE),
    (2, 'Modern Apartment', 'A stylish apartment in the city center.', 2, 200.00, TRUE, FALSE),
    (3, 'Beach House', 'A large house by the beach.', 8, 300.00, TRUE, TRUE);
    """

    insert_reservations = """
    INSERT INTO reservations (room_id, guest_id, check_in, check_out) VALUES 
    (1, 1, '2024-06-01', '2024-06-07'),
    (2, 2, '2024-07-15', '2024-07-20'),
    (3, 3, '2024-08-10', '2024-08-15');
    """

    insert_reviews = """
    INSERT INTO reviews (room_id, guest_id, rating, comment) VALUES 
    (1, 1, 5, 'Amazing place!'),
    (2, 2, 4, 'Great, no parking :(.'),
    (3, 3, 3, 'A lot of noize...');
    """

    analytic_query = """
    SELECT u.user_id, u.username, COUNT(r.reservation_id) AS reservation_count
    FROM users u
    JOIN reservations r ON u.user_id = r.guest_id
    GROUP BY u.user_id, u.username
    ORDER BY reservation_count DESC
    LIMIT 1;
    """

    try:
        cur = connection.cursor()

        cur.execute(create_users_table)
        cur.execute(create_hosts_table)
        cur.execute(create_rooms_table)
        cur.execute(create_reservations_table)
        cur.execute(create_reviews_table)

        cur.execute(insert_users)
        cur.execute(insert_hosts)
        cur.execute(insert_rooms)
        cur.execute(insert_reservations)
        cur.execute(insert_reviews)

        connection.commit()

        cur.execute(analytic_query)
        result = cur.fetchone()
        print("User with the most reservations:")
        print(f"User ID: {result[0]}, Username: {result[1]}, Number of Reservations: {result[2]}")

        print("Tables are done!!!")
    except Exception as e:
        print("[INFO] Error while working with PostgreSQL:", e)
    finally:
        if connection:
            connection.close()
            print("[INFO] PostgreSQL connection closed")


create_tables_and_insert_data()
