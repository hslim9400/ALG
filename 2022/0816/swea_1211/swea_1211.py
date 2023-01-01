import sys
sys.stdin = open('input.txt', 'r')
for tc in range(10):
    test_case = int(input())
    board = [[0]*102]
    line = list(map(int, input().split()))
    board.append([0] + line + [0])
    starts = []
    ends = []
    for j in range(100):
        if line[j] == 1:
            starts.append([j, 0])
    for i in range(98):
        board.append([0] + list(map(int, input().split())) + [0])
    line = list(map(int, input().split()))
    for j in range(100):
        if line[j] == 1:
            ends.append(j)
    board += [[0] * 102]

    dr = [1, 0, 0]
    dc = [0, 1, -1]
    for start in starts:
        hor_move = 0
        r = 1
        c = start[0]
        while r < 100:
            r = r+1
            if board[r][c + 1] == 1:
                while True:
                    hor_move += 1
                    c = c + 1
                    if board[r][c + 1] == 0:
                        break
            elif board[r][c - 1] == 1:
                while True:
                    hor_move += 1
                    c = c - 1
                    if board[r][c - 1] == 0:
                        break
            else:
                pass
        start[1] = hor_move
    starts.sort(key=lambda x: (x[1], -x[0]))
    print(f'#{test_case} {starts[0][0]}')
