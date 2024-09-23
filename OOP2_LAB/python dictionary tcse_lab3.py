#using dictionary
new = {
    'name': 'refat',
    'city': 'Darshona',
    'country': 'bangladesh',
    'age': 23,
    'color': ['red','black','white']
}
print(new)

#using constructor
new2 = dict(name = 'refat',
           salary = 600000)
print(new2)

n = new['name']
c = new['color']
print(n)
print(type(n))
#usign get() method
print(new.get('color'))
print(type(c))

#to get keys
x = new.keys()
print(x)
#to get values using values() method
y = new.values()
print(y)
#to get dictionary keye and values!
z = new.items()
print(z)

if 'name' in new:
    print("yes its present!")
else:
    print("not present!")

#to update
new['name'] = 'pasha'
print(new)

#using update() method
new.update({'name':'agun', 'salary': 3000000000})
print(new)

#to delete usnig pop() method
new.pop('name')
print(new)

#to delete last item using popitem() method
new.popitem()
print(new)

#to delete item using del
del new['age']
print(new)

#to delete entire dict using clear() method
"""new.clear()
print(new)"""


#loop in dictionary
new3 = {
    'name': 'refat',
    'city': 'Darshona',
    'country': 'bangladesh',
    'age': 23,
    'color': ['red','black','white']
}
for i in new3:
    print(i)

##using keys() method to get the values
for i in new3.keys():
    print(i)
#using values() method to get the values
for i in new3.values():
    print(i)
#using items() method to get all the values
for i in new3.items():
    print(i)

#using items() method to get all the values in i, j format
for i , j in new3.items():
    print(i, j)


#dictionary copy

#copy using copy() method
new4 = new3.copy()
print(new4)
#copy using dict() method
new5 = dict(new3)

