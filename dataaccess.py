# data access and data storage
import sqlite3

# DataBaseManagement class to insert queries into and select from database
# There are only 4 products currently in the database (Bag, Pants, Cap, T-shirt)
class DataBaseManagement:
    def __init__(self, path):
        self.conn = sqlite3.connect(path)
        self.cur = self.conn.cursor()
        self.cur.executescript("""

            CREATE TABLE Customer (

                CustomerId integer primary key,
                CustomerFirstName text,
                CustomerLastName text
            );
        
            CREATE TABLE Basket(

                BasketId integer primary key,
                OrderDate text,
                SumPrice float,
                CustomerId REFERENCES Customer (CustomerId)
            );
        
            CREATE TABLE Product(

                ProductId integer primary key,
                ProductName text
            );
            
            CREATE TABLE Product_Price(

                ProductPriceId integer primary key,
                ProductId REFERENCES Product (ProductId),
                ProductPrice float
            );
        
            CREATE TABLE Basket_Product(

                BasketProductId integer primary key,
                ProductId REFERENCES Product (ProductId),   
                BasketId REFERENCES Basket (BasketId)

            );

            INSERT INTO Product (ProductName) VALUES ('Bag');
            INSERT INTO Product (ProductName) VALUES ('T-shirt');
            INSERT INTO Product (ProductName) VALUES ('Pants');
            INSERT INTO Product (ProductName) VALUES ('Cap');

            INSERT INTO Product_Price (ProductId, ProductPrice) VALUES (1, 805000);
            INSERT INTO Product_Price (ProductId, ProductPrice) VALUES (2, 140000);
            INSERT INTO Product_Price (ProductId, ProductPrice) VALUES (3, 340000);
            INSERT INTO Product_Price (ProductId, ProductPrice) VALUES (4, 110000);

        """)
    
# insert into query
    def insert(self, query):
        self.cur.execute(query)
        self.conn.commit()

# select from query
    def show(self, query):
        return self.cur.execute(query).fetchall()