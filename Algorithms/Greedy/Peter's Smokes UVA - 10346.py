

while True:
    try:
        total_cig,k = list(map(int,input().split()))
        total = total_cig
        b = total_cig
        while b>= k:
            total = total+b//k
            b = (b//k) + (b%k)
        print(total)
    except EOFError:
        break