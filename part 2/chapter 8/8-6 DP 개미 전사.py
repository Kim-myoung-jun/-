# 8-6 DP 개미 전사
n = int(input())
data = list(map(int, input().split()))

dp = [0] * n
dp[0] = data[0]
dp[1] = max(data[0], data[1])

for i in range(2, n):
    dp[i] = max(dp[i-2] + data[i], dp[i-1])
print(dp[n-1])