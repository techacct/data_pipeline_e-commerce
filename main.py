import csv
import sqlite3

# Step 1: Extract data from CSV files
sales_data_file = 'sales_data.csv'
product_data_file = 'product_data.csv'
user_data_file = 'user_data.csv'
delivery_data_file = 'delivery_data.csv'

sales_data = []
product_data = []
user_data = []
delivery_data = []

# Read Sales Data
with open(sales_data_file, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        sales_data.append(row)

# Read Product Data
with open(product_data_file, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        product_data.append(row)

# Read User Data
with open(user_data_file, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        user_data.append(row)

# Read Delivery Data
with open(delivery_data_file, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        delivery_data.append(row)
        