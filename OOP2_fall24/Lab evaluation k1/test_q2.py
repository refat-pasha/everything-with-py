class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    def edisplay(self):
        print(f"Employee Name :{self.name} \nSalary : {self.salary}")
class Manager(Employee):
    def __init__(self,name,salary,dept):
        self.name = name
        self.salary = salary
        self.dept = dept
    def mdisplay(self):
        print(f"Manager name : {self.name} \nSalary : {self.salary}\nDept. :{self.dept}")

x = Manager("refat",30000000000,"IT")
x.edisplay()
x.mdisplay()