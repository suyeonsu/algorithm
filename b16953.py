import sys

a, b = map(int, sys.stdin.readline().split())
cnt = 1
while b >= 1:
    if b == a: 
        print(cnt)
        break
    if b % 10 == 1:     # 가장 오른쪽 자리가 1
        b = int(b / 10)
    else:
        b = int(b / 2) if b % 2 == 0 else 0 # 2로 나누어 떨어지지 않으면 while문 중단
    cnt += 1
else:
    print(-1) 
