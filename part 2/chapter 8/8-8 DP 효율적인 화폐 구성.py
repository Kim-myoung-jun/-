# 8-8 DP 효율적인 화폐 구성
import sys
n, m = map(int, sys.stdin.readline().split())
money = []
for _ in range(n):
    money.append(int(sys.stdin.readline()))
    
dp = [10001] * (m+1)
dp[0] = 0
for i in range(1, m+1):
    if i in money:
        dp[i] = 1
    else:
        for j in range(n-1, 0, -1):
            if i - money[j] < 0:
                continue
            else:
                if dp[i-money[j]] != 10001:
                   dp[i] = dp[i-money[j]] + 1
                   break
if dp[m] == 10001:
    print(-1)
else:
    print(dp[m])