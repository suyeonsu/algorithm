from itertools import permutations

def solution(numbers):
    nums = set()
    nums.update([int(''.join(x)) for i in range(1, len(numbers)+1) for x in list(permutations(numbers, i))])

    answer = 0
    for x in nums:
        if x == 0 or x == 1: continue
        elif x == 2: answer += 1
        else:
            for i in range(2, x//2):
                if x % i == 0: break
            else: answer += 1
    return answer
  
  
# 그리고 멋진 풀이.. 

from itertools import permutations

def solution(n):
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))
    a -= set(range(0, 2))
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i))
    return len(a)
