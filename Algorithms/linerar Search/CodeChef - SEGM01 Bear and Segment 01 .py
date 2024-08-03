


"""
a = int(input())
x = '001111110'
for i in range (a):
    b = input()
    if b == int(x) or b == 1111:
        print("YES")
    else:
        print("NO")

"""
for i in range(int(input())):
        S = input().strip('0')
        if '0' not in S and '1' in S:
            print('YES')
        else:
            print('NO')
