




for i in range(1,int(input())+1):
    a = list(map(int,input().split()))
    m= sorted(a)
    n = str(m)[1:-1]
    n = n.replace(",","")

    print(f"Case {i}:",n)


