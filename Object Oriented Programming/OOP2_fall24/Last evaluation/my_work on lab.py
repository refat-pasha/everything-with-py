from abc import ABC, abstractmethod

class Order(ABC):
    @abstractmethod
    def calculate_total(self):
        pass
    @abstractmethod
    def get_order_details(self):
        pass



class OnlineOrder(Order):
    def __init__(self,order_id,name,price,quantity,delivery_charge):
        self.order_id = order_id
        self.name = name
        self.price = price
        self.quantity = quantity
        self.delivery_charge = delivery_charge

    def calculate_total(self,price,quantity,delivery_charge):
        total = 0
        total = (price*quantity)+delivery_charge
        print(f"Total price: {total}")

    def get_order_details(self,order_id,name,price,quantity):
        items = [name,price,quantity]
        print(f"Online Order ID : {order_id}\n"
              f"Items:{items}\n")





class InStoreOrder(Order):
    def __init__(self,order_id,name,price,quantity,delivery_charge):
        self.order_id = order_id
        self.name = name
        self.price = price
        self.quantity = quantity
        self.delivery_charge = delivery_charge

    def items(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def discount(self,percentage):
        self.percentage = percentage

    def calculate_total(self,price,quantity,percentage):
        total = 0
        total = price*quantity
        total = total*(percentage/100)
        total += (total+price)
        print(f"Total price: {total}")

    def get_order_details(self,order_id,name,price,quantity,discount):
        items = [name, quantity, discount]
        print(f"In-Store Order ID : {order_id}\n"
              f"Items:{items}\n")


obj1 = OnlineOrder("xyz","laptop",1000,5,30)
obj1.get_order_details("xyz","laptop",1000,5)
obj1.get_order_details("xyz","mouse",50,2)
obj1.calculate_total(1000,1,25)
obj1.calculate_total(50,2,0)
print()
obj2 = InStoreOrder("abc","monitor",300,1,30)
obj2.get_order_details("abc","monitor",300,1,10)
obj2.calculate_total(300,1,10)

