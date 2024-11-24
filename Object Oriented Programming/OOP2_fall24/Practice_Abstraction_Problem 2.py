# Problem 2:


from abc import ABC,abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.area()

    def area(self):
        self.Rect_area = self.width*self.height


    def display(self):
        print(f"Area of Rectangle: {self.Rect_area}")

class Circle(Shape):
    def __init__(self,radius,pi = 3.1416):
        self.radius = radius
        self.pi = pi
        self.area()

    def area(self):
        self.Circle_area = self.pi*(self.radius*self.radius)

    def display(self):
        print(f"Area of Circle: {self.Circle_area}")


obj = Rectangle(5,10)
obj.display()
obj2 = Circle(4)
obj2.display()
