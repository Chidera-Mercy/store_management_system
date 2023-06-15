"""
The Fashion Boutique Management System is designed to help boutique owners 
manage their inventory, track sales, and maintain customer records. 
The objective of the project is to provide an efficient and organized solution 
for managing various aspects of a fashion boutique, 
ensuring smooth operations and improved customer service.
"""

class Product:
    """
    Represents a product in the inventory of a fashion boutique.
    """
    
    def __init__(self, product_name, product_description, product_price, product_quantity):
        """
        Initializes a new instance of the Product class.

        Args:
            name (str): The name of the product.
            description (str): A description of the product.
            price (float): The price of the product.
            quantity (int): The quantity of the product in the inventory.
        """
        self.name = product_name
        self.description = product_description
        self.price = product_price
        self.quantity = product_quantity

class Inventory:
    """
    Manages the inventory of products in a fashion boutique.
    """
    __all_products = []

    @classmethod
    def add_product(cls, product):
        """
        Adds a product to the inventory.

        Args:
            product (Product): The product to be added to the inventory.
        """
        if product not in cls.__all_products:
            cls.__all_products.append(product)

    @classmethod
    def update_quantity(cls, product_name, new_quantity):
        """
        Updates the quantity of a product in the inventory.

        Args:
            product_name (str): The name of the product.
            new_quantity (int): The new quantity of the product.
        """
        for product in cls.__all_products:
            if product.name == product_name:
                product.quantity = new_quantity
                break

    @classmethod
    def get_product(cls, product_name):
        """
        Retrieves the information of a product from the inventory.

        Args:
            product_name (str): The name of the product.

        Returns:
            None: If the product is not found in the inventory.
        """
        product = next((product for product in cls.__all_products if product_name == product.name), None)
        if product:
            return {
                "Product Name" : product.name,
                "Product Description" : product.description,
                "Product Price" : product.price,
                "Quantity Available" : product.quantity
            }
        else:
            return None

    @classmethod
    def get_available_products(cls):
        """
        Retrieves a list of products that are currently available in the inventory.

        Returns:
            List[Product]: A list of available products.
        """
        return [product for product in cls.__all_products if product.quantity > 0]

class Customer:
    """
    Represents a customer of the fashion boutique.
    """
    __all_customers = []
    def __init__(self, customer_name, customer_email):
        """
        Initializes a new instance of the Customer class.

        Args:
            customer_name (str): The name of the customer.
            customer_email (str): The email address of the customer.
        """
        self.name = customer_name
        self.email = customer_email
        self.customer = {"name": customer_name, "email": customer_email}
        self.__all_customers.append(self.customer)

    __purchase_history = []
    @classmethod
    def add_purchase_history(cls, customer, product, quantity):
        """
        Adds a purchase to the customer's purchase history.

        Args:
            customer (Customer): The customer making the purchase.
            product (Product): The product being purchased.
            quantity (int): The quantity of the product being purchased.
        """
        purchase = (customer, product, quantity)
        cls.__purchase_history.append(purchase)

class Sales:
    """
    Manages the sales records of the fashion boutique.
    """
    __sales_made = []

    @staticmethod
    def make_and_record_sale(product, quantity, customer):
        """
        Processes a sale and records it in the sales records.

        Args:
            product (Product): The product being sold.
            quantity (int): The quantity of the product being sold.
            customer (Customer): The customer making the purchase.
        """
        Inventory.update_quantity(product.name, product.quantity - quantity)
        Customer.add_purchase_history(customer, product, quantity)
        Sales.__sales_made.append((product, quantity, customer))

    @classmethod
    def generate_sales_report(cls):
        """
        Generates a sales report with the recorded sales.

        Returns:
            None: If there are no recorded sales.
        """
        return cls.__sales_made

def main():
    """
    instances can be created and methods can be called here"""

if __name__ == "__main__":
    main()