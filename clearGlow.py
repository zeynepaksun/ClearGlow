import sqlite3

def init_database():
    conn = sqlite3.connect('clearGlow.db')
    cursor = conn.cursor

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
                   id INTEGER PRIMARY KEY,
                   name TEXT NOT NULL,
                   brand TEXT,
                   product_type TEXT,
                   skin_type TEXT,
                   description TEXT
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS routines (
                   id INTEGER PRIMARY KEY,
                   name TEXT NOT NULL,
                   description TEXT
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS favourites (
                   id,
                   user_id,
                   product_id,
                   FOREIGN KEY (product_id) REFERENCES products(id)
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
                   id INTEGER PRIMARY KEY,
                   username TEXT NOT NULL UNIQUE,
                   password TEXT NOT NULL
    )
    ''')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_database()