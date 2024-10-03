"""
3. Create an inner function to
calculate the addition in the following way

• Create an outer function that will
accept two parameters, a and b
• Create an inner function inside an outer function
that will calculate the addition of a and b
• At last, an outer function will
add 5 into addition and return it
"""

def outer_func(a,b):
    def inner_func():
        return a+b
    result = inner_func()
    result += 5
    return result
print(outer_func(4,5))







