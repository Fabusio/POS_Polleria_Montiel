# Archivo: src/setup_db.py
import sqlite3

# Crear la base de datos y la tabla
connection = sqlite3.connect('products.db')
cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        simbologia TEXT NOT NULL,
        variantes TEXT NOT NULL,
        precio REAL NOT NULL
    )
''')

# Insertar datos de prueba
products = [
    ('Pollo Entero', 'POLL', 'Grill, Frito, Asado', 120.0),
    ('Pechuga', 'PECH', 'Asado, Empanizado', 70.0),
    ('Alitas', 'ALIT', 'BBQ, Picante', 50.0),
]

cursor.executemany('''
    INSERT INTO products (nombre, simbologia, variantes, precio) VALUES (?, ?, ?, ?)
''', products)

connection.commit()
connection.close()
