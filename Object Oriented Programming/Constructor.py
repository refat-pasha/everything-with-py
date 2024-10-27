class Students: #class
    roll = "" #
    gpa = "" #
    def __init__(self, roll,gpa): #constructor/spacial type of method
        self.roll= roll
        self.gpa = gpa
    def display(self): #method
        print(f"Roll: {self.roll}, GPA: {self.gpa}")


rahim = Students(101,3.77) #object
rahim.display()

kahim = Students(102,3.70) #object
kahim.display()

