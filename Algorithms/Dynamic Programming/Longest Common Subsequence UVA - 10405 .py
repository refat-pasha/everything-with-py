"""import sys

def solve (a,b):
    a = list(a)
    b = list(b)

    dp = [[0 for _ in range(len(a)+1)] for _ in range(len(b)+1) ]

    for i in range(1, len(b)+1):
        for j in range(1, len(a)+1):
            if(a[j-1] == b[i-1]):
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])
    return dp[len(b)][len(a)]


inn = sys.stdin.read().splitlines()
for i in range(0,len(inn), 2):
    print(solve(inn[i],inn[i+1]))

"""
import sys

def solve(a, b):
    a = list(a)
    b= list(b)
    dp = [[0 for _ in range (len(a)+1)] for _ in range (len(b) + 1)]
    for i in range (1, len(b)+1):

        for j in range (1, len(a)+1):
            if(a[j-1] == b[i-1]):
                dp[i][j] = 1 dp[i-1][j-1]

            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])

    return dp[len(b)] [len (a)]

inn = sys.stdin.read().splitlines()

for i in range(0, len(inn), 2):
    print(solve (inn [i], inn[i+1]))