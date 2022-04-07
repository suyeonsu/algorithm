n, k = map(int, input().split())
cnt = 0
while n != 1:
    if n % k == 0: 
        n /= k
        cnt += 1
    else: 
        n -= n % k
        cnt += n % k
print(cnt)
