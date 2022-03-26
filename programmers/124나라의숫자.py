def to124(n):
    if n == 1: return '1'
    elif n == 2: return '2'
    elif n == 3: return '4'
    else:
        if n % 3 == 0:
            return to124(n//3-1) + '4'
        else:
            return to124(n//3) + str(n%3)

def solution(n):
    return to124(n)
