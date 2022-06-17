from itertools import combinations

while True:
    k = list(input().split())
    if k[0] == '0': break
    s = k[1:]
    for c in combinations(s, 6):
        print(' '.join(list(c)))
    print()
