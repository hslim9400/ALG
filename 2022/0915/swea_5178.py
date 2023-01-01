def calculate(target):
    if not left[target]:
        return tree[target]
    left_res = calculate(left[target])
    right_res = calculate(right[target])
    return left_res + right_res


T = int(input())
for test_case in range(1, T+1):
    N, M, L = map(int, input().split())
    tree = [0] * (N+1)
    left = [0] * (N+1)
    right = [0] * (N+1)
    for i in range(1, N//2+1):
        left[i] = 2*i
        if 2*i+1 > N:
            continue
        right[i] = 2*i + 1
    for i in range(M):
        node, value = map(int, input().split())
        tree[node] = value

    ans = calculate(L)
    print(f'#{test_case} {ans}')
