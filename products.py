# id | name | description| price

from db import conn, cursor

def create_table_products():
    query = """
        CREATE TABLE IF NOT EXISTS products (
            id SERIAL PRIMARY KEY,
            name VARCHAR,
            price INTEGER,
            photo VARCHAR,
            color VARCHAR,
            brand VARCHAR,
            call_back VARCHAR
        );"""
    cursor.execute(query=query)
    conn.commit()

def inseert_product(name: str,
                    description: str,
                    price: int,
                    photo: str,
                    color: str):
    query = f"""
        INSERT INTO product (
            name, description, price, photo, color
        )VALUES(
            '{name}', '{description}', {price}, '{photo}', '{color}
        );'"""
    cursor.execute(query=query)
    conn.cursor()