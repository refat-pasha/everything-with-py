print("hello world")
print("A" *10)
first = "refat"
last = "pasha"
full = f"{first} {last}"
print(full)
print(10**3)


a = int(input())
b = int(input())

print( "X =" ,(a+b))

""" #Sequence IJ 2
for i in range(1,10,2):
    for j in range(7,4,-1):
        print("I={} J={}".format(i,j))
        """

#Sequence IJ 3

for i in range(1,10,2):
    for j in range(6+i,3+i,-1):
        print("I={} J={}".format(i,j))