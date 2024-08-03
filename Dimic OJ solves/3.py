



#solve but not accepted
"""for i in range(1000,0,-1):
    if i%5==1:
        print(i,end='\n')
    else:
        print(i,end='\t')
"""
#accepted
for i in range(1000, 0, -5):
    for j in range(i, max(0, i - 5), -1):
        print(j, end='\t')
    print()
