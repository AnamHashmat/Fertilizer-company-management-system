class Product:
    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock

    def update_stock(self, quantity):
        self.stock += quantity
        class Supplier:
            def __init__(self, supplier_id, name, contact):
                self.supplier_id = supplier_id
                self.name = name
                self.contact = contact

            def __str__(self):
                return f"Supplier[ID: {self.supplier_id}, Name: {self.name}, Contact: {self.contact}]"
    def __str__(self):
        return f"Product[ID: {self.product_id}, Name: {self.name}, Price: {self.price}, Stock: {self.stock}]"


class Customer:
    def __init__(self, customer_id, name, contact):
        self.customer_id = customer_id
        self.name = name
        self.contact = contact

    def __str__(self):
        return f"Customer[ID: {self.customer_id}, Name: {self.name}, Contact: {self.contact}]"


class Order:
    def __init__(self, order_id, customer, products):
        self.order_id = order_id
        self.customer = customer
        self.products = products  # List of tuples (Product, quantity)
        self.total_price = self.calculate_total()

    def calculate_total(self):
        return sum(product.price * quantity for product, quantity in self.products)

    def __str__(self):
        product_details = ", ".join([f"{product.name} (x{quantity})" for product, quantity in self.products])
        return f"Order[ID: {self.order_id}, Customer: {self.customer.name}, Products: {product_details}, Total: {self.total_price}]"


class FertilizerCompany:
    def __init__(self):
        self.products = {}
        self.customers = {}
        self.orders = {}

    def add_product(self, product):
        self.products[product.product_id] = product

    def add_customer(self, customer):
        self.customers[customer.customer_id] = customer

    def create_order(self, order_id, customer_id, product_quantities):
        if customer_id not in self.customers:
            raise ValueError("Customer not found")
        customer = self.customers[customer_id]
        products = []
        for product_id, quantity in product_quantities.items():
            if product_id not in self.products:
                raise ValueError(f"Product ID {product_id} not found")
            product = self.products[product_id]
            if product.stock < quantity:
                raise ValueError(f"Insufficient stock for product {product.name}")
            product.update_stock(-quantity)
            products.append((product, quantity))
        order = Order(order_id, customer, products)
        self.orders[order_id] = order
        return order

    def __str__(self):
        return f"FertilizerCompany[Products: {len(self.products)}, Customers: {len(self.customers)}, Orders: {len(self.orders)}]"