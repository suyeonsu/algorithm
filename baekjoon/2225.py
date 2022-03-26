import sys

n, k = map(int, sys.stdin.readline().split())
dp = [1] * (n+1)    # 정수 1개로 n을 만드는 경우의 수는 항상 1

for i in range(1, k):
    dp[1] = i   # 정수 k개로 1을 만드는 경우의 수는 항상 k -> 'k-1개의 0, 1개의 1' 조합
    for i in range(1, n+1):
        dp[i] = dp[i-1] + dp[i]
print(dp[n] % 1000000000)

# dp[i][j] = dp[i-1][j] + dp[i][j-1] 이라는 점화식이 도출됨
# 메모리 효율을 위해 1차원 배열 사용
