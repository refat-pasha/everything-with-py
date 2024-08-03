


c = 0
a = int(input())
h_uni,g_uni = list(),list()

for i in range (a):
    h,g = input().split(" ")
    h_uni.append(h)
    g_uni.append(g)
for h in (h_uni):
    c+= g_uni.count(h)
print(c)