
#fibonacci series using while
"""
n1,n2 = 0,1
count = 0
nterms = int(input())
while count <nterms :
    print(n1)
    nth = n1+n2
    n1 = n2
    n2 = nth
    count+=1

"""


n = int(input())


#fibonacci
#0,1,1,2,3,5
#number of the fibonacci series position
def fibonacci(n):
    if n ==1 or n==2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print("position of the ",n,"th number in fibonacci:",fibonacci(n))

print("  ")


#fibonacci series:
def fibonacci_series(n):
     if n<= 1:
         return n
     else:
         return fibonacci_series(n-1) + fibonacci_series(n-2)

for i in range(n):
    print(fibonacci_series(i))
