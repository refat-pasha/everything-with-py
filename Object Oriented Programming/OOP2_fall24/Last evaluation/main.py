

from abc import ABC, abstractmethod

class Order(ABC):
    @abstractmethod
    def calculate_total(self):
        pass

    @abstractmethod
    def get_order_details(self):
        pass


class OnlineOrder(Order):
    def __init__(self, order_id, delivery_charge):
        self.order_id = order_id
        self.items = []  # To store multiple items
        self.delivery_charge = delivery_charge

    def add_item(self, name, price, quantity):
        self.items.append({"name": name, "price": price, "quantity": quantity})

    def calculate_total(self):
        total = sum(item['price'] * item['quantity'] for item in self.items) + self.delivery_charge
        return total

    def get_order_details(self):
        print(f"Online Order ID: {self.order_id}")
        print("Items:")
        for item in self.items:
            print(f"  {item['name']}: ${item['price']} x {item['quantity']}")
        print(f"Delivery Charge: ${self.delivery_charge}")
        print(f"Total: ${self.calculate_total()}")


class InStoreOrder(Order):
    def __init__(self, order_id, discount=0):
        self.order_id = order_id
        self.items = []  # To store multiple items
        self.discount = discount  # Discount as a percentage

    def add_item(self, name, price, quantity):
        self.items.append({"name": name, "price": price, "quantity": quantity})

    def calculate_total(self):
        subtotal = sum(item['price'] * item['quantity'] for item in self.items)
        total = subtotal - (subtotal * self.discount / 100)
        return total

    def get_order_details(self):
        print(f"In-Store Order ID: {self.order_id}")
        print("Items:")
        for item in self.items:
            print(f"  {item['name']}: ${item['price']} x {item['quantity']}")
        print(f"Discount: {self.discount}%")
        print(f"Total: ${self.calculate_total()}")




# Online Order
online_order = OnlineOrder("xyz", delivery_charge=25)
online_order.add_item("Laptop", 1000, 1)
online_order.add_item("Mouse", 50, 2)
online_order.get_order_details()

print("\n")

# In-Store Order
in_store_order = InStoreOrder("abc", discount=10)
in_store_order.add_item("Monitor", 300, 1)
in_store_order.add_item("Keyboard", 100, 1)
in_store_order.get_order_details()
