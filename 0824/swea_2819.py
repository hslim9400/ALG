def next_num(current, num):
    if len(num) == 7:
        nums.add(num)
        return

    for d in range(4):
        if 0 <= current[0] + dr[d] < 4 and 0 <= current[1] + dc[d] < 4:
            current[0], current[1] = current[0] + dr[d], current[1] + dc[d]
            num += board[current[0]][current[1]]
            next_num(current, num)
            current[0], current[1] = current[0] - dr[d], current[1] - dc[d]
            num = num[:-1]


T = int(input())
for test_case in range(1, T+1):
    board = []
    for _ in range(4):
        board.append(input().split())

    dc = [1, 0, -1, 0]
    dr = [0, 1, 0, -1]
    nums = set()
    for i in range(4):
        for j in range(4):
            next_num([i,j], '')

    ans = len(nums)
    print(f'#{test_case} {ans}')