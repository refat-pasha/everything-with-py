class Phone: #Phone is parent class
    def call(self):
        print("You can Call")
    def message(self):
        print("You can message")
    def photo(self):
        print("You can capture photo")
class Brand(Phone): #Brand is child class/sub-class
    def functions(self):
        print("name of functions are :")


a = Brand()
a.functions()
a.photo()
a.call()
a.message()