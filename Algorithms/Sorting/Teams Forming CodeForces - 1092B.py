a = int(input())
b = list(map(int,input().split()))
b.sort()

c= 0
for i in range(0,len(b),2):
    c +=b[i+1]-b[i]
print(c)

