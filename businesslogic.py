# business logic
import dataaccess as da

# connecting to the database
my_db = da.DataBaseManagement('three_layered_db.db')

# Product class 
# initialize a class with customer profile and name of the product
class Product:
    basket_id = 1
    def __init__(self, first_name, last_name, product_name):
        self.first_name, self.last_name, self.product_name = first_name, last_name, product_name

    def __str__(self):
        return self.first_name + ' ' + self.last_name + ' ' + self.product_name

# inserting a query into the database
    def insert(self):
        check_customer_existance = True
        try:
            customer_id = my_db.show(f"""
                    SELECT c.CustomerId FROM Customer as c WHERE CustomerFirstName="{self.first_name}"\
                            AND CustomerLastName="{self.last_name}"
                    """).pop()[0]
        except IndexError:
            check_customer_existance = False

        product_id = my_db.show(f"""
                                SELECT p.ProductId FROM Product as p WHERE ProductName="{self.product_name}"
                        """).pop()[0]

        price = my_db.show(f"""
                        SELECT pp.ProductPrice FROM Product_Price as pp INNER JOIN Product as p ON pp.ProductId=p.ProductId 
                        WHERE ProductName="{self.product_name}"
                """).pop()[0]

        if  not check_customer_existance:   
            my_db.insert(f"""INSERT INTO Customer (CustomerFirstName, CustomerLastName) VALUES \
                            ("{self.first_name}", "{self.last_name}")""")

            customer_id = my_db.show(f"""
                    SELECT c.CustomerId FROM Customer as c WHERE CustomerFirstName="{self.first_name}"\
                            AND CustomerLastName="{self.last_name}"
                    """).pop()[0]

            my_db.insert(f"""INSERT INTO Basket (CustomerId, OrderDate, SumPrice) VALUES \
                        ({customer_id}, date('now'), {price} \
                            )""")

            my_db.insert(f"""INSERT INTO Basket_Product (BasketId, ProductId) VALUES ({Product.basket_id}, {product_id})""")
            Product.basket_id += 1

        else:
            my_db.insert(f"""INSERT INTO Basket (CustomerId, OrderDate, SumPrice) VALUES \
            ({customer_id}, date('now'), {price} \
                )""")

            my_db.insert(f"""INSERT INTO Basket_Product (BasketId, ProductId) VALUES ({Product.basket_id}, {product_id})""")
            Product.basket_id += 1


# showing the queries inserted by the user
    @staticmethod
    def show():
        q = my_db.show(f"""
                SELECT c.CustomerFirstName, c.CustomerLastName, p.ProductName, pp.ProductPrice FROM Customer as c \
                INNER JOIN Basket as b ON c.CustomerId=b.CustomerId INNER JOIN Basket_Product as bp ON b.BasketId=bp.BasketId 
                INNER JOIN Product as p ON p.ProductId = bp.ProductId INNER JOIN Product_Price as pp ON 
                pp.ProductId=p.ProductId;
            """)
                                
        return q

# showing what are the products a customer has bought
    @staticmethod
    def show_history(fullname):
        q = my_db.show(f"""SELECT p.ProductName, pp.ProductPrice FROM Customer as c \
            INNER JOIN Basket as b ON c.CustomerId=b.CustomerId INNER JOIN Basket_Product as bp ON b.BasketId=bp.BasketId 
            INNER JOIN Product as p ON p.ProductId = bp.ProductId INNER JOIN Product_Price as pp ON 
            pp.ProductId=p.ProductId WHERE c.CustomerFirstName="{fullname[0]}" AND c.CustomerLastName="{fullname[1]}"
            """)
        return q