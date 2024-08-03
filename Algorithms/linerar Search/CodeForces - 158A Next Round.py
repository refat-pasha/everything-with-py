




c, pos = map(int, input().split(' '))
sc = list(map(int, input().split(' ')))

advanced = 0
for point in sc:
    if point >= sc[pos-1] and point != 0:
        advanced += 1

print(advanced)
