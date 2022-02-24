import sys

"""
시계 방향(반시계는 화살표 반대로)
주 대각선 -> 가운데 열
가운데 열 -> 부 대각선
부 대각선 -> 가운데 행
가운데 행 -> 주 대각선

i는 0 ~ n-1
주 대각선: (i, i)
가운데 열: (i, n//2)
부 대각선: (i, n-1-i)
가운데 행: (n//2, i)
"""

T = int(sys.stdin.readline())
for _ in range(T):
    n, d = map(int, sys.stdin.readline().split())
    board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    
    w = [board[i][i] for i in range(n)]     # 주 대각선
    x = [board[i][n//2] for i in range(n)]  # 가운데 열
    y = [board[i][n-1-i] for i in range(n)] # 부 대각선
    z = [board[n//2][i] for i in range(n)]  # 가운데 행

    if d >= 0:  # cw
        for k in range(d//45): w, x, y, z = z, w, x, y[::-1]
    else:       # ccw
        for k in range(-d//45): w, x, y, z = x, y, z[::-1], w
    
    # 배열에 반영
    for i in range(n): 
        board[i][i] = w[i]
        board[i][n//2] = x[i]
        board[i][n-1-i] = y[i]
        board[n//2][i] = z[i]
    
    for b in board:
        print(' '.join(map(str, b)))
