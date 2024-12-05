# Archivo: src/app.py
from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Conexión a la base de datos
def get_db_connection():
    conn = sqlite3.connect('products.db')
    conn.row_factory = sqlite3.Row
    return conn

# Endpoint para buscar productos
@app.route('/search', methods=['GET'])
def search_products():
    query = request.args.get('q', '').lower()  # Obtener el término de búsqueda
    conn = get_db_connection()
    products = conn.execute(
        "SELECT * FROM products WHERE lower(nombre) LIKE ? OR lower(simbologia) LIKE ?",
        (f'%{query}%', f'%{query}%')
    ).fetchall()
    conn.close()
    return jsonify([dict(product) for product in products])

if __name__ == '__main__':
    app.run(debug=True)
