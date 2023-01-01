def find_coord(n):
    if n == 1:
        return 1, 1
    group = int((2*n+0.25)**0.5+0.499)
    group_last = sum(range(group+1))
    which = group_last - n
    return group - which, 1 + which


def find_num(coords):
    if coords == (1,1):
        return 1
    group = coords[0] + coords[1] - 1
    group_last = sum(range(group+1))
    which = coords[1]-1
    return group_last - which


T = int(input())

for test_case in range(1, T+1):
    p, q = map(int, input().split())

    step_1_a = find_coord(p)
    step_1_b = find_coord(q)
    step_1 = (step_1_a[0] + step_1_b[0], step_1_a[1] + step_1_b[1])
    step_2 = find_num(step_1)

    print(f'#{test_case} {step_2}')

