def make_comb(depth, picked, left, k):
    global min_diff
    if depth == N//2:
        food_1 = 0
        food_2 = 0
        for i in range(N//2-1):
            for j in range(i+1, N//2):
                food_1 += board[picked[i]][picked[j]] + board[picked[j]][picked[i]]
                food_2 += board[left[i]][left[j]] + board[left[j]][left[i]]
        diff = abs(food_1 - food_2)
        if diff < min_diff:
            min_diff = diff
        return

    new_picked = list(picked)
    new_left = list(left)
    for i in range(k+1, N):
        if i in new_picked:
            continue
        new_picked.append(i)
        new_left.remove(i)
        make_comb(depth+1, new_picked, new_left, i)
        new_picked.remove(i)
        new_left.append(i)


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    board = []
    for _ in range(N):
        board.append(list(map(int, input().split())))

    min_diff = 20000 * N * N
    make_comb(0, [], list(range(N)), 0)
    print(f'#{test_case} {min_diff}')
