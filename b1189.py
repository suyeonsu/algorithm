import sys

dx = [-1, 0, 0, 1] # 위, 오른쪽, 왼쪽, 아래
dy = [0, 1, -1, 0] # 위, 오른쪽, 왼쪽, 아래

def dfs(x, y, dist):
    global cnt

    if x == 0 and y == c-1 and dist == k: 
        cnt += 1
    else:
        for d in zip(dx, dy):
            xx, yy = x + d[0], y + d[1]
            if 0 <= xx < r and 0 <= yy < c and board[xx][yy] == '.' and not visited[xx][yy]:
                visited[xx][yy] = 1
                dfs(xx, yy, dist+1)
                visited[xx][yy] = 0

if __name__ == '__main__':
    # 시작지점: (r-1, 0) 목표지점: (0, c-1)
    r, c, k = map(int, sys.stdin.readline().split())
    board = [list(sys.stdin.readline().rstrip()) for _ in range(r)]
    visited = [[0] * c for _ in range(r)]
    cnt = 0

    visited[r-1][0] = 1
    dfs(r-1, 0, 1)
    print(cnt)
