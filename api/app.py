from flask import Flask, jsonify, request
import psycopg2
import os

app = Flask(__name__)

# Database connection
def get_db_connection():
    conn = psycopg2.connect(
        host=os.getenv('DB_HOST', 'localhost'),
        database=os.getenv('DB_NAME', 'shopfast'),
        user=os.getenv('DB_USER', 'admin'),
        password=os.getenv('DB_PASSWORD', 'password')
    )
    return conn

@app.route('/')
def home():
    return jsonify({
        "service": "ShopFast API",
        "version": "1.0",
        "status": "running"
    })

@app.route('/health')
def health():
    try:
        conn = get_db_connection()
        conn.close()
        return jsonify({"status": "healthy", "database": "connected"}), 200
    except Exception as e:
        return jsonify({"status": "unhealthy", "error": str(e)}), 500

@app.route('/products')
def get_products():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT * FROM products;')
        products = cur.fetchall()
        cur.close()
        conn.close()
        
        return jsonify({
            "products": [
                {"id": p[0], "name": p[1], "price": float(p[2])} 
                for p in products
            ]
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/products', methods=['POST'])
def add_product():
    data = request.json
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            'INSERT INTO products (name, price) VALUES (%s, %s) RETURNING id;',
            (data['name'], data['price'])
        )
        product_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({"id": product_id, "message": "Product added"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

