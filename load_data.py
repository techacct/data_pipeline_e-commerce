import psycopg2



# Establish a connection to the PostgreSQL database
conn = psycopg2.connect(
    host="localhost",
    database="test_db",
    user="root",
    password="root"
)
cur = conn.cursor()



# load data into the database
def load_data():

    # Load User Data
    cur.execute("CREATE TABLE IF NOT EXISTS user_data (UserID INT PRIMARY KEY, UserName VARCHAR, Email VARCHAR, SignupDate DATE, LastLogin DATE);")
    cur.executemany("INSERT INTO user_data VALUES (%s, %s, %s, %s, %s);", user_data)

    # Load Product Data
    cur.execute("CREATE TABLE IF NOT EXISTS product_data (ProductID INT PRIMARY KEY, ProductName VARCHAR, Category VARCHAR, ListPrice INT);")
    cur.executemany("INSERT INTO product_data VALUES (%s, %s, %s, %s);", product_data)

    # Load Sales Data
    cur.execute("CREATE TABLE IF NOT EXISTS sales_data (OrderID INT PRIMARY KEY, ProductID INT, UserID INT, Quantity INT, OrderDate DATE, UnitPrice INT, FOREIGN KEY (ProductID) REFERENCES product_data(ProductID), FOREIGN KEY (UserID) REFERENCES user_data(UserID));")
    cur.executemany("INSERT INTO sales_data VALUES (%s, %s, %s, %s, %s, %s);", sales_data)

    # Generate and Load Delivery Data
    cur.execute("CREATE TABLE IF NOT EXISTS delivery_data (OrderID INT, DeliveryPartner VARCHAR, DeliveryDate DATE, DeliveryStatus VARCHAR, FOREIGN KEY (OrderID) REFERENCES sales_data(OrderID));")
    cur.executemany("INSERT INTO delivery_data VALUES (%s, %s, %s, %s);", delivery_data)

    # Commit the changes and close the database connection
    conn.commit()
    cur.close()
    conn.close()

load_data()
