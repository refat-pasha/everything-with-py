



def binary_search(arr,low,high,item):
    if low <= high:
        mid = (low+high)//2
        if arr[mid] == item:
            return mid
        elif arr[mid] >item:
            return binary_search(arr,low,mid-1,item)
        else:
            return binary_search(arr,mid+1,high,item)
    else:
        return -1


arr = list(map(int,input().split()))
arr = sorted(arr)
target = int(input())
print(binary_search(arr,0,len(arr)-1,target))


