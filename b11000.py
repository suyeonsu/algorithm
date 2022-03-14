import sys
import heapq

n = int(sys.stdin.readline())
a = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
a.sort(key=lambda x:(x[0], x[1]))

hq = []
heapq.heappush(hq, a[0][1])
for i in range(1, n):
    if hq[0] <= a[i][0]:    # 종료 시간 <= 다음 시작 시간
        heapq.heappop(hq)   # 강의실 수 늘어나지 않음
    heapq.heappush(hq, a[i][1])
print(len(hq))
