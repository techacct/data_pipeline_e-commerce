import random
from faker import Faker
import psycopg2

fake = Faker()

# Establish a connection to the PostgreSQL database
conn = psycopg2.connect(
    host="localhost",
    database="your_database_name",
    user="your_username",
    password="your_password"
)
cur = conn.cursor()

# Generate Sales Data
def generate_sales_data(num_records):
    sales_data = []
    for _ in range(num_records):
        order_id = fake.random_int(min=1000, max=9999)
        product_id = fake.random_int(min=1000, max=9999)
        user_id = fake.random_int(min=1000, max=9999)
        quantity = fake.random_int(min=1, max=10)
        order_date = fake.date_between(start_date='-1y', end_date='today')
        unit_price = fake.random_int(min=10, max=100)
        sales_data.append([order_id, product_id, user_id, quantity, order_date, unit_price])
    return sales_data

# Generate Product Data
def generate_product_data(num_records):
    categories = ['Electronics', 'Clothing', 'Home Appliances', 'Books', 'Beauty']
    product_data = []
    for _ in range(num_records):
        product_id = fake.random_int(min=1000, max=9999)
        product_name = fake.word() + " " + fake.word()
        category = random.choice(categories)
        list_price = fake.random_int(min=50, max=500)
        product_data.append([product_id, product_name, category, list_price])
    return product_data

# Generate User Data
def generate_user_data(num_records):
    user_data = []
    for _ in range(num_records):
        user_id = fake.random_int(min=1000, max=9999)
        username = fake.user_name()
        email = fake.email()
        signup_date = fake.date_between(start_date='-2y', end_date='-1y')
        last_login = fake.date_between(start_date='-1y', end_date='today')
        user_data.append([user_id, username, email, signup_date, last_login])
    return user_data

# Generate Delivery Data
def generate_delivery_data(num_records, order_ids):
    delivery_partners = ['FedEx', 'UPS', 'DHL', 'USPS']
    delivery_data = []
    for order_id in order_ids:
        delivery_partner = random.choice(delivery_partners)
        delivery_date = fake.date_between(start_date='today', end_date='+7d')
        delivery_status = random.choice(['Delivered', 'In Transit', 'Pending'])
        delivery_data.append([order_id, delivery_partner, delivery_date, delivery_status])
    return delivery_data

# Generate and load data into the database
def generate_and_load_data():
    num_records = 1000

    # Generate data
    sales_data = generate_sales_data(num_records)
    product_data = generate_product_data(num_records)
    user_data = generate_user_data(num_records)

    # Load User Data
    cur.execute("CREATE TABLE IF NOT EXISTS user_data (UserID INT PRIMARY KEY, UserName VARCHAR, Email VARCHAR, SignupDate DATE, LastLogin DATE);")
    cur.executemany("INSERT INTO user_data VALUES (%s, %s, %s, %s, %s);", user_data)

    # Load Product Data
    cur.execute("CREATE TABLE IF NOT EXISTS product_data (ProductID INT PRIMARY KEY, ProductName VARCHAR, Category VARCHAR, ListPrice INT);")
    cur.executemany("INSERT INTO product_data VALUES (%s, %s, %s, %s);", product_data)

    # Load Sales Data
    cur.execute("CREATE TABLE IF NOT EXISTS sales_data (OrderID INT PRIMARY KEY, ProductID INT, UserID INT, Quantity INT, OrderDate DATE, UnitPrice INT, FOREIGN KEY (ProductID) REFERENCES product_data(ProductID), FOREIGN KEY (UserID) REFERENCES user_data(UserID));")
    cur.executemany("INSERT INTO sales_data VALUES (%s, %s, %s, %s, %s, %s);", sales_data)

    # Get the order IDs for generating delivery data
    order_ids = [record[0] for record in sales_data]

    # Generate and Load Delivery Data
    delivery_data = generate_delivery_data(num_records, order_ids)
    cur.execute("CREATE TABLE IF NOT EXISTS delivery_data (OrderID INT, DeliveryPartner VARCHAR, DeliveryDate DATE, DeliveryStatus VARCHAR, FOREIGN KEY (OrderID) REFERENCES sales_data(OrderID));")
    cur.executemany("INSERT INTO delivery_data VALUES (%s, %s, %s, %s);", delivery_data)

    # Commit the changes and close the database connection
    conn.commit()
    cur.close()
    conn.close()

generate_and_load_data()
