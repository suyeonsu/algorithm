# 처음에 풀이한 코드
""" 
n, m = map(int, input().split())
know = set(map(int, input().rstrip()[2:].split()))
party = [list(map(int, input().rstrip()[2:].split())) for _ in range(m)]

for repeat in range(m):
    for i in range(m):
        if any(x in know for x in party[i]):
            know.update(party[i])
            party[i] = []
            i = 0
print(m-party.count([]))
"""

# 집합 자료형을 사용해 불필요한 연산을 줄임
n, m = map(int, input().split())
know = set(input().rstrip()[1:].split())
party = [set(input().rstrip()[1:].split()) for _ in range(m)]

for _ in range(m):
    for i, p in enumerate(party):
        if p & know:
            know.update(p)
            party[i] = set()
print(m - party.count(set()))
