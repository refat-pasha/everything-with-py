


import math
a = int(input())
for i in range(1,a+1):
    b = int(input())
    if math.ceil(math.sqrt(b)) == math.floor(math.sqrt(b)):
        print("YES")
    else:
        print("NO")



