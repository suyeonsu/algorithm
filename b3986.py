n = int(input())
cnt = 0
for _ in range(n):
    word = input()
    st = []
    for x in word:
        if st:
            if st[-1] == x:
                st.pop()
            else:
                st.append(x)
        else:
            st.append(x)
    if len(st) == 0: cnt += 1
print(cnt)
