T = 10
for test_case in range(1, T+1):
    N = int(input())
    target = input()
    pairs = {')': '(', ']': '[', '}': '{', '>': '<'}
    openers = ['(', '[', '{', '<']
    stack = []
    for i in range(N):
        if target[i] in openers:
            stack.append(target[i])
        else:
            if pairs[target[i]] not in stack:
                ans = 0
                break
            else:
                stack.remove(pairs[target[i]])
    if stack:
        ans = 0
    else:
        ans = 1
    print(f'#{test_case} {ans}')