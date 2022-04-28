d1 = [(-1, 0), (0, -1), (0, 1), (1, 0)]
d2 = [(-2, 0), (-1, -1), (-1, 1), (0, -2), (0, 2), (1, -1), (1, 1), (2, 0)]

def solution(places):
    answer = [1, 1, 1, 1, 1]
    for n, p in enumerate(places):
        seat = [(i, j) for i in range(5) for j in range(5) if p[i][j] == 'P']
        for x, y in seat:
            if any(p[x+dx][y+dy] == 'P' for dx, dy in d1 if 0 <= x+dx < 5 and 0 <= y+dy < 5):
                answer[n] = 0
                break
            for dx, dy in d2:
                xx, yy = x+dx, y+dy
                if 0 <= xx < 5 and 0 <= yy < 5 and p[xx][yy] == 'P':
                    a = set((x+dx, y+dy) for dx, dy in d1 if 0 <= x+dx < 5 and 0 <= y+dy < 5)
                    b = set((xx+dx, yy+dy) for dx, dy in d1)
                    if any(p[r][c] != 'X' for r, c in list(a & b)):
                        answer[n] = 0
                        break
    return answer
