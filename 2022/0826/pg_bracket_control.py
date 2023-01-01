def is_proper(s):
    stack = []
    for i in s:
        if i == '(':
            stack.append(i)
        else:
            if stack:
                stack.pop()
            else:
                return False
    if stack:
        return False
    else:
        return True


def proper_brackets(s):
    if is_proper(s):
        return s
    for i in range(1, len(s)+1):
        if s[:i].count('(') == s[:i].count(')'):
            u = s[:i]
            v = s[i:]
            break
    v = proper_brackets(v)
    if is_proper(u):
        s = u + v
        return s

    new = '(' + v + ')'
    u = u[1:-1]
    for i in u:
        if i == '(':
            new += ')'
        else:
            new += '('
    s = new
    return s


def solution(p):
    answer = proper_brackets(p)

    return answer


print(solution(""))
