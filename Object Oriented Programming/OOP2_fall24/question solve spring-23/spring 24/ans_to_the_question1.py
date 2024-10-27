#required parameter
"""def hello(name):
    return f"hello {name}"
print(hello("refat"))
"""
#default parameter
"""def hello(name='refat'):
    return f"hello {name}"
print(hello())"""

#variable length parameter
def add_number(*args):
    return sum(args)
print(add_number(5,6,7,3,3,3,))
"""
"""
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")



