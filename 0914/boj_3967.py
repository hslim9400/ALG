def next_blank(depth):
    global nums, counts, ans, flag
    if flag:
        return

    if depth == 12:
        ans = nums[:]
        flag = True
        return

    if nums[depth]:
        next_blank(depth+1)
        return

    for i in range(1, 13):
        if counts[i]:
            continue
        nums[depth] = i
        combs = [
            nums[0] + nums[2] + nums[5] + nums[7],
            nums[1] + nums[2] + nums[3] + nums[4],
            nums[0] + nums[3] + nums[6] + nums[10],
            nums[7] + nums[8] + nums[9] + nums[10],
            nums[1] + nums[5] + nums[8] + nums[11],
            nums[4] + nums[6] + nums[9] + nums[11]
        ]
        if max(combs) > 26:
            nums[depth] = 0
            continue
        counts[i] = 1
        next_blank(depth+1)
        counts[i] = 0
        nums[depth] = 0


board = []
blanks = 0
alps = {'x': 0, 'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12,
        1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H', 9: 'I', 10: 'J', 11: 'K', 12: 'L'}
counts = [0] * 13
nums = []
for _ in range(5):
    line = list(input())
    board.append(line)
    for something in line:
        if something in alps.keys():
            counts[alps[something]] += 1
            nums.append(alps[something])
ans = []
flag = False
next_blank(0)
for i in range(5):
    for j in range(9):
        if board[i][j] != '.':
            board[i][j] = alps[ans.pop(0)]
    print(''.join(board[i]))
