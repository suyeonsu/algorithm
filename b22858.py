import sys

n, k = map(int, sys.stdin.readline().split())
s = list(map(int, sys.stdin.readline().split()))
d = list(map(int, sys.stdin.readline().split()))

p = [0] * n
while k:
    for i in range(n):
        p[d[i]-1] = s[i]
    s[:] = p[:] # 왜 슬라이싱 말고 s = p는 대입이 안될까..
    k -= 1
for pi in p: print(pi, end=' ')
