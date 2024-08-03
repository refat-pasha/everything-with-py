

t = int(input())
for i in range(1,t+1):
    a = input()
    b = a[::-1]
    if a == b:
        print(f"Case {i}: Yes")
    else:
        print(f"Case {i}: No")

