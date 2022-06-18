n = int(input())
dp = [int(input())]
for _ in range(n-1):
    tmp = list(map(int, input().split()))
    for i in range(len(tmp)):
        if i == 0: tmp[0] += dp[0]
        elif i == len(tmp)-1: tmp[-1] += dp[-1]
        else: tmp[i] += max(dp[i-1], dp[i])
    dp = tmp
print(max(dp))
