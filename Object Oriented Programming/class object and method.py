class Students: #class
    roll = "" #
    gpa = "" #
    def set_value(self, roll,gpa): #method
        self.roll= roll
        self.gpa = gpa
    def display(self): #method
        print(f"Roll: {self.roll}, GPA: {self.gpa}")


rahim = Students() #object
rahim.set_value(101,3.77)
rahim.display()

kahim = Students() #object
kahim.set_value(102,3.70)
kahim.display()






#class object and methods example
class workers:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
       print(f"Name : {self.name} and Age: {self.age}")

w1 = workers("Nana",69)
w1.display()


#inharitance example

class shape: #parent class
    def height(self):
        print("this is the height of a triangle")
    def weight(self):
        print("this is the weight of a triangle")
class point(shape): #child class
    def doshomik(self):
        print("this is a doshomik(0.5)")

x1 = point()
x1.doshomik()
x1.height()
x1.weight()











