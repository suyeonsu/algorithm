import sys

s = sys.stdin.readline().split('-')
if len(s) <= 1:
    s = map(int, s[0].split('+'))
    print(sum(s))
else:
    s = [sum(map(int, x.split('+'))) for x in s]
    print(s[0] - sum(s[1:]))
