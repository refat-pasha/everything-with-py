



def linerar_search(arr,item):
    for i in range (len(arr)):
        if arr[i] == item:
          return i
    return -1

arr = list(map(int,input().split()))
target = int(input())
print(linerar_search(arr,target))


