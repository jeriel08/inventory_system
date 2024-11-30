import mysql.connector

def connect_db():
    try:
        conn = mysql.connector.connect( host='localhost',
                                        user='root',
                                        database='inventory_system' )
        return conn
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def close_connection(connection):
    if connection.is_connected():
        connection.close()

# User Functions
def insert_user(username, password, contact_number, email_address, birthday, gender):
    connection = connect_db()
    cursor = connection.cursor()

    query = """
    INSERT INTO users (username, password, contact_number, email, birthdate, gender, created_at)
    VALUES (%s, %s, %s, %s, %s, %s, NOW())
    """

    cursor.execute(query, (username, password, contact_number, email_address, birthday, gender))
    connection.commit()

    close_connection(connection)

def update_user(user_id, username, password, contact_number, email, birthdate, gender):
    try:
        connection = connect_db()
        cursor = connection.cursor()
        query = """
            UPDATE users
            SET username = %s, password = %s, contact_number = %s, email = %s, birthdate = %s, gender = %s, updated_at = NOW()
            WHERE user_id = %s
        """
        cursor.execute(query, (username, password, contact_number, email, birthdate, gender, user_id))
        connection.commit()

        close_connection(connection)

        return True
    except Exception as e:
        print(f"Error updating user: {e}")
        return False

def check_user(username):
    connection = connect_db()
    cursor = connection.cursor(dictionary=True)

    query = "SELECT * FROM users WHERE username = %s"
    cursor.execute(query, (username,))

    user = cursor.fetchone()

    cursor.close()
    connection.close()

    return user

# Product Functions
def add_product(product_name, price, quantity, category, supplier_id, user_id):
    connection = connect_db()
    cursor = connection.cursor()
    query = "INSERT INTO products (product_name, price, quantity, category, supplier_id, user_id, created_at) VALUES (%s, %s, %s, %s, %s, %s, NOW())"
    cursor.execute(query, (product_name, float(price), int(quantity), category, supplier_id, user_id))
    connection.commit()
    close_connection(connection)

def update_product(product_id, product_name, category, price, quantity, supplier_id):
    connection = connect_db()
    cursor = connection.cursor()
    query = """
        UPDATE products
        SET product_name = %s, category = %s, price = %s, quantity = %s, supplier_id = %s, updated_at = NOW()
        WHERE product_id = %s
    """
    cursor.execute(query, (product_name, category, price, quantity, supplier_id, product_id))
    connection.commit()
    rows_affected = cursor.rowcount
    close_connection(connection)
    return rows_affected > 0

def delete_product(product_name):
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM products WHERE product_name = %s", (product_name,))
    rows_affected = cursor.rowcount
    connection.commit()
    close_connection(connection)
    return rows_affected > 0

def get_product_by_name(product_name):
    connection = connect_db()
    cursor = connection.cursor(dictionary=True)
    query = "SELECT * FROM products WHERE product_name = %s"
    cursor.execute(query, (product_name,))
    result = cursor.fetchone()
    close_connection(connection)
    return result

def fetch_product_name():
    connection = connect_db()
    cursor = connection.cursor()
    query = "SELECT product_name FROM products ORDER BY product_name"
    cursor.execute(query)
    product_names = [row[0] for row in cursor.fetchall()]  # Returns an empty list if no products exist
    close_connection(connection)
    return product_names


def fetch_product_detail(product_name):
    db = connect_db()
    cursor = db.cursor()
    query = """
            SELECT p.category, p.quantity, p.price, s.supplier_name, s.contact_number
            FROM Products p            
            JOIN Suppliers s ON p.supplier_id = s.supplier_id            
            WHERE p.product_name = %s            
            """
    cursor.execute(query, (product_name,))
    product_details = cursor.fetchone()
    db.close()
    return product_details

# Supplier Functions
def add_supplier(supplier_name, supplier_contact):
    connection = connect_db()
    cursor = connection.cursor()
    query = "INSERT INTO suppliers (supplier_name, contact_number) VALUES (%s, %s)"
    cursor.execute(query, (supplier_name, supplier_contact))
    connection.commit()
    supplier_id = cursor.lastrowid
    close_connection(connection)
    return supplier_id

def update_supplier(supplier_id, supplier_name, contact_number):
    connection = connect_db()
    cursor = connection.cursor()
    query = "UPDATE suppliers SET supplier_name = %s, contact_number = %s WHERE supplier_id = %s"
    cursor.execute(query, (supplier_name, contact_number, supplier_id))
    connection.commit()
    close_connection(connection)


def delete_supplier(supplier_id):
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM suppliers WHERE supplier_id = %s", (supplier_id,))
    connection.commit()
    close_connection(connection)

def get_supplier_by_name(supplier_name):
    connection = connect_db()
    cursor = connection.cursor(dictionary=True)
    query = "SELECT supplier_id, supplier_name, contact_number FROM suppliers WHERE supplier_name = %s"
    cursor.execute(query, (supplier_name,))
    result = cursor.fetchone()
    close_connection(connection)
    return result


# General Utility
def fetch_inventory_data():
    connection = connect_db()
    cursor = connection.cursor()
    query = """
        SELECT
            p.product_id,
            p.product_name,
            p.price,
            p.quantity,
            p.category,
            p.created_at,
            s.supplier_id,
            s.supplier_name,
            s.contact_number
        FROM
            products p
        LEFT JOIN
            suppliers s ON p.supplier_id = s.supplier_id
        ORDER BY p.product_id
    """
    cursor.execute(query)
    data = cursor.fetchall()
    close_connection(connection)
    return data

# Clear Operation
def clear_inventory(include_suppliers=False):
    connection = connect_db()
    cursor = connection.cursor()

    try:
        cursor.execute("DELETE FROM products;")
        cursor.execute("ALTER TABLE products AUTO_INCREMENT = 2000;")

        if include_suppliers:
            cursor.execute("DELETE FROM suppliers WHERE supplier_id NOT IN (SELECT supplier_id FROM products);")
            cursor.execute("ALTER TABLE products AUTO_INCREMENT = 3000;")

        connection.commit()
        success = True
    except Exception as e:
        connection.rollback()
        print(f"Error clearing inventory: {e}")
        success = False
    finally:
        close_connection(connection)

    return success


