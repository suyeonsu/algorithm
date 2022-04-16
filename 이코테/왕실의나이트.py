d = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]
y, x = input()

cnt = 0
for dx, dy in d:
    xx, yy = int(x) + dx, chr(ord(y) + dy)
    if 1 <= xx <= 8 and 'a' <= yy <= 'h':
        cnt += 1
print(cnt)
