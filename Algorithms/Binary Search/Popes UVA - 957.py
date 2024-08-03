


import bisect

def solve():
    years = int(input())
    pope = int(input())
     
    popes = []
    for i in range(pope):
        popes.append(int(input()))
    
    max_i = 0
    max_s = None
    max_e = None
    for i , p in enumerate(popes):
        lower_bound = p - years
        lower_i = bisect.bisect_right(popes, lower_bound)
        if i - lower_i > max_i:
            max_i = i - lower_i
            max_s = popes[lower_i]
            max_e = p
    print(max_i+1 , max_s,max_e)
while True:
    try:
        solve()
        input()
    except EOFError:
        break




