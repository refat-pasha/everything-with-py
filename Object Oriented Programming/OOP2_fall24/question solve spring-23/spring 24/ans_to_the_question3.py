#3.a
"""
#vul
#numbers = (1,2,3)
#numbers[1] = 5
#print(numbers)

#right code
numbers = [1,2,3]
numbers[1] = 5
print(numbers)

#or

numbers = (1, 2, 3)
number = list[numbers]
print(number)

#output: [1,5,3]
"""
#3.b
import random
n = []
for i in range(0, 11):
    n.append(random.randint(0, 100))
for j in range(50, 100):
    for z in n:
        if z == j:
            print(z, end=" ")


