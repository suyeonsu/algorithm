def solution(s):
    l = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for num, eng in enumerate(l):
        if s.isdecimal(): break
        s = s.replace(eng, str(num))
    return int(s)
