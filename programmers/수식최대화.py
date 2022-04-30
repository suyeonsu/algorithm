from itertools import permutations

def toPostfix(expression, priority):
    postfix = []
    op = []
    for e in expression:
        if e.isdecimal(): postfix.append(eval(e))
        else:
            while op and priority[op[-1]] <= priority[e]: postfix.append(op.pop())
            op.append(e)
    return postfix + op[::-1] if op else postfix

def calc(expression):
    st = []
    for e in expression:
        if type(e) == int: st.append(e)
        else: 
            b, a = st.pop(), st.pop()
            if e == '+': st.append(a + b)
            elif e == '-': st.append(a - b)
            else: st.append(a * b)
    return abs(st.pop())

def solution(expression):
    answer = 0
    oper = [x for x in ['+', '-', '*'] if x in expression]
    for old, new in zip(['-', '+', '*'], [' - ', ' + ', ' * ']): expression = expression.replace(old, new)
    expression = expression.split()

    cases = list(permutations(oper, len(oper)))
    for case in cases:
        priority = {oper:i for i, oper in enumerate(list(case))}
        postfix = toPostfix(expression, priority)
        answer = max(answer, calc(postfix))
    return answer
