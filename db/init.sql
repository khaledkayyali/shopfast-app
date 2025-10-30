CREATE TABLE IF NOT EXISTS products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO products (name, price) VALUES
    ('Laptop Pro 15"', 1299.99),
    ('Wireless Mouse', 29.99),
    ('Mechanical Keyboard', 89.99),
    ('4K Monitor', 449.99),
    ('USB-C Hub', 49.99);

GRANT ALL PRIVILEGES ON TABLE products TO admin;
GRANT ALL PRIVILEGES ON SEQUENCE products_id_seq TO admin;
