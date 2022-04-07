n, m, k = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort(reverse=True)
answer = 0
tmp = k
for _ in range(m):
    if tmp == 0:
        answer += nums[1]
        tmp = k
    else:
        answer += nums[0]
        tmp -= 1
print(answer)
