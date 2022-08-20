dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def dfs(x, y):
    for d in zip(dx, dy):
        xx, yy = x+d[0], y+d[1]
        if 0 <= xx < n and 0 <= yy < m and board[xx][yy] == '0':
            board[xx][yy] = '1'
            dfs(xx, yy)

n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]
cnt = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == '0':
            board[i][j] = '1'
            dfs(i, j)
            cnt += 1
print(cnt)
