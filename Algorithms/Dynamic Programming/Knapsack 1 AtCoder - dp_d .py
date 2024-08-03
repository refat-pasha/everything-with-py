"""import sys

input = sys.stdin.readline

n, w = list(map(int, input().split()))
arr = [tuple(map(int, input().split())) for _ in range(n)]

dp = []
dp.append([[] for _ in range(w + 1)])
dp.append([0] * (w + 1))
dp[0][0] = arr
ans = 0

for i in range(w + 1):
    for wj, vj in dp[0][i]:
        if i + wj <= w and dp[1][i] + vj > dp[1][i + wj]:
            remaining = [x[:] for x in dp[0][i]]
            remaining.remove((wj, vj))
            dp[0][i + wj] = remaining
            dp[1][i + wj] = dp[1][i] + vj
    ans = max(ans, dp[1][i])

print(ans)
"""
import sys

input = sys.stdin.readline

n, w = map(int, input().split())
arr = [tuple(map(int, input().split())) for _ in range(n)]

dp = [0] * (w + 1)

for i in range(n):
    weight, value = arr[i]
    for j in range(w, weight - 1, -1):
        dp[j] = max(dp[j], dp[j - weight] + value)

print(dp[w])
