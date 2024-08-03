kan = int(input())
lis = []
for i in range(kan):
    s = int(input())
    lis.append(s)
lis.sort()
i =0 
j= kan//2

count = 0
while j< kan and i< kan //2:
    if (lis[i]*2) <= lis[j]:
        count = count + 1
        i = i+1
        j = j+1
    else:
        j = j+1
print(kan - count)

