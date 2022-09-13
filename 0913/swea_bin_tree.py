def make_bin(num):
    ans = ''
    target = num
    while target:
        left = target % 2
        ans = str(left) + ans
        target //= 2
    return ans


T = int(input())
for test_case in range(1, T+1):
    N, V = map(int, input().split())
    n = make_bin(N)
    v = make_bin(V)
    if n[:2] == '10':
        dist_left = len(n)-1
        dist_right = len(n)-2
    else:
        dist_left = len(n)-1
        dist_right = len(n)-1

    if v[:2] == '10':
        total_dist = len(v)-1 + dist_right
    else:
        total_dist = len(v)-1 + dist_left
    print(f'#{test_case} {total_dist}')
