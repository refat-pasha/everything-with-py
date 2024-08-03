



t = int(input())
test = 0

while t > 0:
    t -= 1
    n = int(input())
    a = [0] * 100001
    a[1:n+1] = map(int, input().split())

    k = 0
    ans = 0

    for i in range(1, n+1):
        if a[i] - a[i-1] > k:
            k = a[i] - a[i-1]

    ans = k

    for i in range(1, n+1):
        if a[i] - a[i-1] == k:
            k -= 1
        elif a[i] - a[i-1] > k:
            ans += 1
            break

    test += 1
    print("Case {}: {}".format(test, ans))




