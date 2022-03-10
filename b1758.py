import sys

n = int(sys.stdin.readline())
tip = [int(sys.stdin.readline()) for _ in range(n)]

tip.sort(reverse=True)
tip = [tip[i] - i if tip[i] - i > 0 else 0 for i in range(n)]
print(sum(tip))
