def next_blank(depth):  # 재귀순열 만들기
    global nums, counts, ans, flag
    if flag:
        return

    if depth == 12:  # 작은 알파벳부터 앞에 넣어보므로 완성된 순간 정답조건을 만족
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
        combs = [  # 별 모양의 숫자들을 더하는 규칙
            nums[0] + nums[2] + nums[5] + nums[7],
            nums[1] + nums[2] + nums[3] + nums[4],
            nums[0] + nums[3] + nums[6] + nums[10],
            nums[7] + nums[8] + nums[9] + nums[10],
            nums[1] + nums[5] + nums[8] + nums[11],
            nums[4] + nums[6] + nums[9] + nums[11]
        ]
        if max(combs) > 26:  # 하나라도 26을 넘는 순간 아웃
            # 만약 완성되었는데 26보다 큰 숫자가 없다면 모두 26이다.
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
nums = []  # 덧셈을 위한 리스트
for _ in range(5):
    line = list(input())
    board.append(line)
    for something in line: # 리스트로 받은 애들 중 무언가가
        if something in alps.keys():  # 알파벳이거나 x라면
            counts[alps[something]] += 1  # 체크에 표시하고
            nums.append(alps[something])  # 덧셈리스트에도 넣는다.
ans = []
flag = False  # 답을 찾으면 트루가 되어 인셉션중인 애들 폭파
next_blank(0)
for i in range(5):
    for j in range(9):
        if board[i][j] != '.':
            board[i][j] = alps[ans.pop(0)]  # 찾은 숫자를 알파벳으로
    print(''.join(board[i]))
