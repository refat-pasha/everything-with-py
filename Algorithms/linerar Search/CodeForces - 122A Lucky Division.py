


l = [4,7,47,74,444,447,474,477,744,774,747,777]
n = int(input())
x = False
for i in range (len(l)):
    if n%l[i] == 0:
        x = True
if(x):
    print("YES")
else:
    print("NO")