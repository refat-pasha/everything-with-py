

for ncase in range(int(input())):
    n =int(input())
    arr = input()
    scarecrow, i = 0, 0
    while(i<n):
        if(arr[i] == "."):
            scarecrow += 1
            i +=3
        else:
            i  +=1

    print(f"Case {ncase+1}: {scarecrow}")