def solution(s):
    st = []
    for i in range(len(s)):
        if st and st[-1] == s[i]:
            st.pop()
        else:
            st.append(s[i])
    return 0 if st else 1
