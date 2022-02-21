import math

n = int(input())
dp = [5] * (n+1)
for i in range(1, int(math.sqrt(n))+1):
    dp[i*i] = 1

for i in range(2, n+1):
    if dp[i] != 1:
        for j in range(1, int(math.sqrt(i))+1):
            dp[i] = min(dp[i-j*j] + dp[j*j], dp[i])
print(dp[n])

## python3 시간초과, pypy3 통과
