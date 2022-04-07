n, m = map(int, input().split())
answer = 0
for _ in range(n):
    card = list(map(int, input().split()))
    answer = max(answer, min(card))
print(answer)
