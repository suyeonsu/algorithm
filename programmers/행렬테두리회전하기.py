from collections import deque

def solution(rows, columns, queries):
    answer = []
    m = [[0] * columns for _ in range(rows)]
    inc = 1
    for r in range(rows):
        for c in range(columns):
            m[r][c] = inc
            inc += 1
            
    for q in queries:
        x1, y1, x2, y2 = q[0]-1, q[1]-1, q[2]-1, q[3]-1
        idx = []
        for y in range(y1, y2+1): idx.append((x1, y))
        for x in range(x1+1, x2+1): idx.append((x, y2))
        for y in range(y2-1, y1-1, -1): idx.append((x2, y))
        for x in range(x2-1, x1, -1): idx.append((x, y1))
        
        origin = deque([m[x][y] for x, y in idx])
        origin.appendleft(origin.pop())
        for pos, val in zip(idx, origin): m[pos[0]][pos[1]] = val
        answer.append(min(origin))
        
    return answer
