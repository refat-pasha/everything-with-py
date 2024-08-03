from bisect import bisect_right, bisect_left

T = int(input())
t = 1

while t<=T:
    n,q = (int(x) for x in input().split())
    lis = list((int(x) for x in input().split()))
    length = len(lis)
    print("Case", str(t)+":")
    while q > 0:
        q-=1
        X,Y = (int(x) for x in input().split())
        right = bisect_right(lis ,Y,0,length)
        left = bisect_left(lis,X,0, length)
        print(right-left)
    t=+1


