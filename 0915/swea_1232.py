def calculate(target):
    if tree[target] not in opers:
        return tree[target]

    left_res = calculate(left[target])
    right_res = calculate(right[target])
    if tree[target] == '+':
        return left_res + right_res
    if tree[target] == '-':
        return left_res - right_res
    if tree[target] == '*':
        return left_res * right_res
    if tree[target] == '/':
        return left_res / right_res


T = 10
for test_case in range(1, T+1):
    N = int(input())
    left = [0] * (N+1)
    right = [0] * (N+1)
    opers = {'+', '-', '*', '/'}
    tree = [0] * (N+1)
    for i in range(N):
        node = input().split()
        if node[1] in opers:
            left[int(node[0])] = int(node[2])
            right[int(node[0])] = int(node[3])
            tree[int(node[0])] = node[1]
        else:
            tree[int(node[0])] = int(node[1])

    ans = calculate(1)
    print(f'#{test_case} {int(ans)}')