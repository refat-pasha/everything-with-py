class Phone: #Phone is parent class

    def __init__(self):
        print("I am in Phone Class")#first call


class Brand(Phone): #Brand is child class/sub-class

    def __init__(self):
        super().__init__() #return to super class/parent class
        print("I am in Brand class")#overring call of super class


a = Brand()
