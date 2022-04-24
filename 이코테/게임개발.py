n, m = map(int, input().split())
a, b, d = map(int, input().split())
direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 북, 동, 남, 서
board = [list(map(int, input().split())) for _ in range(n)]

cnt = 0
while True:
    # 네 방향이 모두 바다 -> 멈춤
    if all(board[a+dx][b+dy] == 1 for dx, dy in direction):
        break
    # 바다이거나 이미 방문한 칸 -> 뒤로 한 칸 이동
    elif all(board[a+dx][b+dy] != 0 for dx, dy in direction):
        a = a + direction[d-2][0]
        b = b + direction[d-2][1]
        # 뒤가 바다 -> 멈춤
        if board[a][b] == 1: break
    # 방문하지 않은 칸이 존재
    else:
        for _ in range(4):
            d = d-1 if d else 3
            aa, bb = a + direction[d][0], b + direction[d][1]
            if 0 < aa < n and 0 < bb < m and board[aa][bb] == 0:
                a, b = aa, bb
                board[a][b] = -1
                cnt += 1
                break
print(cnt)
