import sqlite3

# Add functions
def add_user(username, password):
    conn = sqlite3.connect('clearGlow.db')
    cursor = conn.cursor()

    cursor.execute('''
    INSERT INTO users (username, password)
    VALUES (?, ?)''', (username, password))

    conn.commit()
    conn.close()

def add_product(name, brand, product_type, skin_type, description):
    conn = sqlite3.connect('clearGlow.db')
    cursor = conn.cursor()

    cursor.execute('''
    INSERT INTO products (name, brand, product_type, skin_type, description)
    VALUES (?, ?, ?, ?, ?)''', (name, brand, product_type, skin_type, description))
    
    conn.commit()
    conn.close()

def add_routine(name, description):
    conn = sqlite3.connect('clearGlow.db')
    cursor = conn.cursor()

    cursor.execute('''
    INSERT INTO routines (name, description)
    VALUES (?, ?)''', (name, description))

    conn.commit()
    conn.close()

def add_favourite(user_id, product_id):
    conn = sqlite3.connect('clearGlow.db')
    cursor = conn.cursor()

    cursor.execute('''
    INSERT INTO favourites (user_id, product_id)
    VALUES (?, ?)''', (user_id, product_id))

    conn.commit()
    conn.close()

# Fetch and check functions

def check_user(username, password):
    conn = sqlite3.connect('clearGlow.db')
    cursor = conn.cursor()

    cursor.execute('''
    SELECT * FROM users WHERE username = ? AND password = ?''', (username, password))

    user = cursor.fetchone()
    conn.close()

    return user

def fetch_products():
    conn = sqlite3.connect('clearGlow.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM products')

    products = cursor.fetchall()
    conn.close()

    return products

def fetch_routines():
    conn = sqlite3.connect('clearGlow.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM routines')

    routines = cursor.fetchall()
    conn.close()

    return routines

def fetch_favourites(user_id):
    conn = sqlite3.connect('clearGlow.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM favourites WHERE user_id = ?', (user_id,))

    favourites = cursor.fetchall()
    conn.close()

    return favourites