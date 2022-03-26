a, b = input(), input()
n, m = len(a), len(b)
dp = [[0] * (n+1) for _ in range(m+1)]

for i in range(1, m+1):
    for j in range(1, n+1):
        if b[i-1] == a[j-1]:
                # 해당 문자 이전 문자열까지의 lcs 길이가 저장된 dp[i-1][j-1]에 1을 더함
                dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
print(dp[-1][-1])
