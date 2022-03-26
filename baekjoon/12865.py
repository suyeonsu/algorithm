import sys

n, k = map(int, sys.stdin.readline().split())
dp = [0] * (k+1)

for _ in range(n):
    w, v = map(int, sys.stdin.readline().split())
    for i in range(k, w-1, -1):
        dp[i] = max(v+dp[i-w], dp[i])
print(dp[k])

# 헐 이거 왜 앞에서부터, 뒤에서부터 결과가 다르지
# range(w, k+1) 이랑 range(k, w-1, -1)이랑 결과가 다르다..

# 냅색 알고리즘
