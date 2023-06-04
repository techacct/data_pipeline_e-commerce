import random
from faker import Faker
import csv

fake = Faker()

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

# Generate and save data to CSV files
def generate_and_save_data():
    num_records = 100000

    sales_data = generate_sales_data(num_records)
    with open('sales_data.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['OrderID', 'ProductID', 'UserID', 'Quantity', 'OrderDate', 'UnitPrice'])
        writer.writerows(sales_data)

    product_data = generate_product_data(num_records)
    with open('product_data.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['ProductID', 'ProductName', 'Category', 'ListPrice'])
        writer.writerows(product_data)

    user_data = generate_user_data(num_records)
    with open('user_data.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['UserID', 'UserName', 'Email', 'SignupDate', 'LastLogin'])
        writer.writerows(user_data)

    order_ids = [record[0] for record in sales_data]
    delivery_data = generate_delivery_data(num_records, order_ids)
    with open('delivery_data.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['OrderID', 'DeliveryPartner', 'DeliveryDate', 'DeliveryStatus'])
        writer.writerows(delivery_data)

generate_and_save_data()
