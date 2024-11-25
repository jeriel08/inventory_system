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
def fetch_users():
    connection = connect_db()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    close_connection(connection)
    return users


def insert_user(username, password, contact_number, email_address, birthday, gender):
    connection = connect_db()
    cursor = connection.cursor()

    # SQL query to insert a new user into the users table
    query = """
    INSERT INTO users (username, password, contact_number, email, birthdate, gender, created_at)
    VALUES (%s, %s, %s, %s, %s, %s, NOW())
    """

    # Execute the query with the user's data
    cursor.execute(query, (username, password, contact_number, email_address, birthday, gender))
    connection.commit()

    close_connection(connection)


def update_user(user_id, username, password, contact_number, email, birthdate, gender):
    try:
        connection = connect_db()
        cursor = connection.cursor()
        query = """
            UPDATE users
            SET username = %s, password = %s, contact_number = %s, email = %s, birthdate = %s, gender = %s
            WHERE user_id = %s
        """
        cursor.execute(query, (username, password, contact_number, email, birthdate, gender, user_id))
        connection.commit()

        close_connection(connection)

        return True
    except Exception as e:
        print(f"Error updating user: {e}")
        return False


def delete_user(user_id):
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM users WHERE user_id = %s", (user_id,))
    connection.commit()
    close_connection(connection)


def check_user(username):
    # Establish database connection
    connection = connect_db()
    cursor = connection.cursor(dictionary=True)  # Use dictionary cursor for key-based access

    # SQL query to find user by username
    query = "SELECT * FROM users WHERE username = %s"
    cursor.execute(query, (username,))

    # Fetch the user data (returns a dictionary or None)
    user = cursor.fetchone()

    # Close the connection
    cursor.close()
    connection.close()

    return user  # This will be None if the user does not exist

# Product Functions
def fetch_products():
    connection = connect_db()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    close_connection(connection)
    return products

def fetch_product_by_id(product_id):
    connection = connect_db()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM products WHERE product_id = %s", (product_id,))
    product = cursor.fetchone()
    close_connection(connection)
    return product

def add_product(product_name, price, quantity, category, supplier_id, user_id):
    connection = connect_db()
    cursor = connection.cursor()
    query = "INSERT INTO products (product_name, price, quantity, category, supplier_id, user_id, created_at) VALUES (%s, %s, %s, %s, %s, %s, NOW())"
    cursor.execute(query, (product_name, int(quantity), float(price), category, supplier_id, user_id))
    connection.commit()
    close_connection(connection)

def update_product(product_id, updated_data):
    connection = connect_db()
    cursor = connection.cursor()
    query = "UPDATE products SET product_name = %s, description = %s, price = %s, quantity = %s, supplier_id = %s WHERE product_id = %s"
    cursor.execute(query, (*updated_data, product_id))  # updated_data is a tuple like (product_name, description, price, quantity, supplier_id)
    connection.commit()
    close_connection(connection)

def delete_product(product_id):
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM products WHERE product_id = %s", (product_id,))
    connection.commit()
    close_connection(connection)

def get_product_by_name(product_name):
    connection = connect_db()
    cursor = connection.cursor(dictionary=True)
    query = "SELECT * FROM products WHERE product_name = %s"
    cursor.execute(query, (product_name,))
    result = cursor.fetchone()
    close_connection(connection)
    return result


# Supplier Functions
def fetch_suppliers():
    connection = connect_db()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM suppliers")
    suppliers = cursor.fetchall()
    close_connection(connection)
    return suppliers

def add_supplier(supplier_name, supplier_contact):
    connection = connect_db()
    cursor = connection.cursor()
    query = "INSERT INTO suppliers (supplier_name, contact_number) VALUES (%s, %s)"
    cursor.execute(query, (supplier_name, supplier_contact))  # supplier_data is a tuple like (supplier_name, contact_info)
    connection.commit()
    supplier_id = cursor.lastrowid
    close_connection(connection)
    return supplier_id

def update_supplier(supplier_id, updated_data):
    connection = connect_db()
    cursor = connection.cursor()
    query = "UPDATE suppliers SET supplier_name = %s, contact_info = %s WHERE supplier_id = %s"
    cursor.execute(query, (*updated_data, supplier_id))  # updated_data is a tuple like (supplier_name, contact_info)
    connection.commit()
    close_connection(connection)

def delete_supplier(supplier_id):
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM suppliers WHERE supplier_id = %s", (supplier_id,))
    connection.commit()
    close_connection(connection)

def get_supplier_by_name_and_contact(supplier_name, contact_info):
    connection = connect_db()
    cursor = connection.cursor(dictionary=True)
    query = "SELECT * FROM suppliers WHERE supplier_name = %s AND contact_info = %s"
    cursor.execute(query, (supplier_name, contact_info))
    result = cursor.fetchone()
    close_connection(connection)
    return result


# General Utility
def fetch_treeview_data():
    connection = connect_db()
    cursor = connection.cursor(dictionary=True)

    query = """
    SELECT p.product_id, p.product_name, p.quantity, p.price, p.supplier_id, 
           s.supplier_name, s.contact_info, p.created_at
    FROM products p
    JOIN suppliers s ON p.supplier_id = s.supplier_id;
    """

    cursor.execute(query)
    data = cursor.fetchall()

    close_connection(connection)

    return data

