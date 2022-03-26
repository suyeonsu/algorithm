def solution(skill, skill_trees):
    cnt = 0
    for st in skill_trees:
        st = list(st)
        now = 0
        while st and now < len(skill):
            if st[0] not in skill:
                st.pop(0)
            else:
                if st[0] == skill[now]:
                    st.pop(0)
                    now += 1
                elif st[0] in skill[:now]: 
                    st.pop(0)
                else: 
                    break
        if now == len(skill) or len(st) == 0: cnt += 1
    return cnt
