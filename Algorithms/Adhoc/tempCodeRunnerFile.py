"""

def number_of_cells(n):
    return 2*n*n-2*n+1
n = int(input().strip())
print(number_of_cells(n))
"""



"""a,b= map(int,input().split())
x = a+b
y = a*b
print(x, y)"""


"""a = int(input())
count = 0
if a>=30:
    count+=3
elif a>=15:
    count+=2
elif a>=5:
    count+=1
print(count)"""


"""a,b = map(int,input().split())
if a>2000 or (a <= 2000 and b > 100):
    print("Bandor, these bananas are tasty enough.")
else:
    print("No Bandor, bananas are not tasty enough.")



"""
"""num = int(input())
print("{:,}".format(num))"""

"""a = int(input())

for i in range(1,a+1):
    if a % i == 0:
        print(i)"""


"""def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib = [0] * (n + 1)
        fib[1] = 1
        for i in range(2, n + 1):
            fib[i] = fib[i - 1] + fib[i - 2]
        return fib[n]

N = int(input())

print(fibonacci(N))"""

"""a,b= map(int,input().split())
print(a/b)"""



a = int(input())
b = 1
for i in range(2,a+1):
    b = (b*i)%10000
print(b)




