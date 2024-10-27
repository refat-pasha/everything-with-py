class Vehicle:
    def __init__(self,seating_capacity):
        self.seating_capacity = seating_capacity
    def fare(self):
        print(f"Fare is : {self.seating_capacity*100}")
class Bus(Vehicle):
    def __init__(self,seating_capacity):
        self.seating_capacity = seating_capacity
    def fare(self):
        total = self.seating_capacity*100
        final_amount = total + total*.1
        print(f"Final amount : {final_amount}")
x = Bus(50)
x.fare()