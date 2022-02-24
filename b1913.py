"""
n = 3 상 우 하 하 좌 좌 / 상 상
n = 5 상 우 하 하 좌 좌 / 상 상 상 우 우 우 하 하 하 하 좌 좌 좌 좌 / 상 상 상 상
n = 7 상 우 하 하 좌 좌 / 상 상 상 우 우 우 하 하 하 하 좌 좌 좌 좌 / 상 상 상 상 상 우 우 우 우 우 하 하 하 하 하 하 좌 좌 좌 좌 좌 좌 / 상 상 상 상 상 상
"""

n = int(input())
num = int(input())
snail = [[0] * n for _ in range(n)]

x, y = n//2, n//2
cnt = 1
snail[x][y] = cnt
for k in range(1, n, 2):
    # up
    for l in range(1, k+1): 
        x -= 1
        cnt += 1
        snail[x][y] = cnt
    # right
    for l in range(1, k+1): 
        y += 1
        cnt += 1
        snail[x][y] = cnt
    # down
    for l in range(1, k+2):
        x += 1
        cnt += 1
        snail[x][y] = cnt
    # left
    for l in range(1, k+2):
        y -= 1
        cnt += 1
        snail[x][y] = cnt
# 마지막 줄 n-1번 up
for k in range(1, n):
    x -= 1
    cnt += 1
    snail[x][y] = cnt

for i in range(n):
    for j in range(n):
        print(snail[i][j], end=' ')
        if snail[i][j] == num: ans = (i+1, j+1)
    print()
print(ans[0], ans[1])
