def op_x(a, b, ans):
    a += 1
    b *= 2
    ans += 'X'
    return a, b, ans


def op_y(a, b, ans):
    a *= 2
    b += 1
    ans += 'Y'
    return a, b, ans


T = int(input())
for test_case in range(1, T+1):
    a, b = map(int, input().split())
    ans = ''
    que = [[a, b, ans]]

    while True:
        current = que.pop(0)
        if max(current[0], current[1]) + (1000 - len(current[2])) \
                > min(current[0], current[1]) * (2**(1000 - len(current[2]))):
            continue
        next_X = op_x(*current)
        if next_X[0] == next_X[1]:
            ans = next_X[2]
            break
        que.append(next_X)

        next_Y = op_y(*current)
        if next_Y[0] == next_Y[1]:
            ans = next_Y[2]
            break
        que.append(next_Y)

    print(f'#{test_case} {ans}')
