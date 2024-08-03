



T = int(input())
for i in range(1, T + 1):
    N = int(input())
    print(f"Case {i}:", end="")
    for j in range(1, N + 1):
        if N % j == 0:
            print(f" {j}", end="")
    print()



