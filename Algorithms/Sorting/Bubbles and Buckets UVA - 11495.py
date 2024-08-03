

count = 0



while arr[0]>0:
    arr = list(map(int, input().split()))
    n = len(arr)
    for i in range(n-1):

        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                count+=1
    if arr[0] == 0:
        break
    print(count)
    if count%2==0:
        print("Marcelo")
    else:
        print("Carlos")






