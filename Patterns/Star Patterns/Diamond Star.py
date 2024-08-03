



#n = int(input()) #if user want to take input
n = 5 #if input preset
for i in range(n-1):
    for j in range(i, n):
        print(' ', end=' ')
    for j in range(i):
        print('*',end=' ')
    for j in range(i+1):
        print('*',end=' ')
    print()
for i in range(n):
    for j in range(i + 1):
        print(' ', end=' ')
    for j in range(i, n - 1):
        print('*', end=' ')
    for j in range(i, n):
        print('*', end=' ')
    print()





