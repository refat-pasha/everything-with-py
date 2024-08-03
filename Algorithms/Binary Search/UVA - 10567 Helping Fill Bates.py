


import bisect

entry = input()
string_s = [[] for i in range (256)]
for i in range (len(entry)):
    string_s[ord(entry[i])].append(i)
int_Q = int(input())
for i in range(int_Q):
    entry = input().strip()
    start = 0
    end = -1
    valid = True
    for i in range(len(entry)):
        c = string_s[ord(entry[i])]
        finalc = bisect.bisect(c,end)
        if finalc == len(c):
            valid = False
            break
        end = c[finalc]
        if i == 0:
            start = end
    if valid:
        print(f"Matched {start} {end}")
    else:
        print("Not matched")





