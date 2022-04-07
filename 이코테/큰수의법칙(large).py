n, m, k = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort(reverse=True)
seq = [nums[0]] * k + [nums[1]]
print(sum(seq)*m//(k+1) + sum(seq[:m%(k+1)]))
