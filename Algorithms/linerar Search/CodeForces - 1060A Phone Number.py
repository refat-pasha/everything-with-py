"""



b = 0, int(input())
Count = 0
a = list(map(int, input().split(' ')))
for i in a:
    if len(a)<10:
        break
    elif len(a)>10 and a.count(8):
        Count+=1
print(Count)

        """

n = int(input())
s = input()
eights = s.count('8')
if eights >= n // 11:
    print(n // 11)
elif eights < n // 11 and n > 11:
    print(eights)
else:
    print(0)



