"""


def firstMethod():
    secondMethod()
    print("I am the first Method")
def secondMethod():
    thirdMethod()
    print("i am the second Method")
def thirdMethod():
    fourthMethod()
    print("I am the third Method")
def fourthMethod():
    print("I am the Fourth Method")

    """

"""
def recursiveMethod(n):
    if n<1:
        print("n is tless than 1")
    else:
        print(n)
        recursiveMethod(n-1)

recursiveMethod(4)

"""



x = int(input())

#factorial using recursion
def factorial(x):
    if x == 1:
        return x
    else:
        return x*factorial(x-1)
print("using recurcion: ",factorial(x))


#factorial  using library
import math
print("using library: ",math.factorial(x))


print("  ")


#print 1 to nth number
def print1toNth(x):
    if x == 0:
        return
    else:
        print1toNth(x-1)
    print("print 1 to nth number :",x)
print1toNth(x)


print("  ")


#print nth to 1 number
def print1toNth(x):
    if x == 0:
        return
    else:
        print("print nth to 1 number :",x)
        print1toNth(x-1)

print1toNth(x)


print("  ")


#sum of nth numbers
def sum_x(x):
    if x == 0:
        return 0
    y = x+sum_x(x-1)
    return y
print("sum of the number is: ",sum_x(x))


print("  ")


