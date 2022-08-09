def dfs(i, s):
    global n, nums, t, answer
    if i == n:
        if s == t: answer += 1
    else:
        dfs(i+1, s+nums[i])
        dfs(i+1, s-nums[i])

def solution(numbers, target):
    global n, nums, t, answer
    answer = 0
    n, nums, t = len(numbers), numbers, target
    dfs(0, 0)
    return answer