import sqlite3
import csv

def get_db_connection():
    conn = sqlite3.connect('market.db')
    conn.row_factory = sqlite3.Row
    return conn

def populate_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Create table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY,
            name TEXT,
            category TEXT,
            price REAL
        )
    ''')
    
    # Clear existing data to prevent UNIQUE constraint errors on reload
    cursor.execute("DELETE FROM products")
    
    # Read CSV and insert
    with open('market_data.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader) # skip header
        for row in reader:
            cursor.execute(
                'INSERT INTO products (id, name, category, price) VALUES (?, ?, ?, ?)',
                (row[0], row[1], row[2], row[3])
            )
    
    conn.commit()
    conn.close()
    print("Database populated successfully.")

def create_product(name, category, price):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO products (name, category, price) VALUES (?, ?, ?)', (name, category, price))
    conn.commit()
    conn.close()
    return cursor.lastrowid

def get_products_by_category(category):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products WHERE category=?", (category,))
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]

def update_product(product_id, name, price):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('UPDATE products SET name=?, price=? WHERE id=?', (name, price, product_id))
    conn.commit()
    conn.close()

def delete_product(product_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM products WHERE id=?', (product_id,))
    conn.commit()
    conn.close()
