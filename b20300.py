import sys

n = int(sys.stdin.readline())
t = list(map(int, sys.stdin.readline().split()))

t.sort()
m = t[-1] # 가장 큰 값 저장
end = -2 if n%2 else -1 # n이 홀수이면 마지막 인덱스는 -2, n이 짝수이면 마지막 인덱스는 -1

# 정렬된 t를 반으로 나눠 (큰 값, 작은 값)으로 짝지어 최소값 계산
for a, b in zip(t[:n//2], t[end:n//2:-1]):
    m = max(m, a+b)
print(m)
