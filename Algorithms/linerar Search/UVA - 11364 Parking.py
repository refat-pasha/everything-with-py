


T = int(input())
for _ in range(T):
    b = int(input())
    L = list(map(int,input().split()))
    L.sort()
    #L.reverse()
    print(2*(L[-1]-L[0]))
