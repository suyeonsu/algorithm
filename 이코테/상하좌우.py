d = {'L':(0, -1), 'R':(0, 1), 'U':(-1, 0), 'D':(1, 0)}

n = int(input())
move = input().split()
x, y = 1, 1
for m in move:
    if 1 <= x + d[m][0] <= n and 1 <= y + d[m][1] <= n:
        x, y = x + d[m][0], y + d[m][1]
print(x, y)
