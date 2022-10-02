
def push(depth, current_max, board):
    global max_num
    if depth == 5:
        if current_max > max_num:
            max_num = current_max
        return

    new_board = list(map(list, zip(*board)))

    for d in range(4):
        target = []
        if d == 0:
            for i in range(N):
                target.append(board[i][:])
        elif d == 1:
            for i in range(N):
                target.append(board[i][::-1])
            pass
        elif d == 2:
            for i in range(N):
                target.append(new_board[i][:])
        else:
            for i in range(N):
                target.append(new_board[i][::-1])

        finished = []
        next_max = current_max
        for i in range(N):
            line = []
            temp = []
            for j in range(N-1, -1, -1):
                if target[i][j] != 0:
                    if temp:
                        if temp[0] == target[i][j]:
                            line.append(temp[0]*2)
                            if temp[0] * 2 > next_max:
                                next_max = temp[0] * 2
                            temp = []
                        else:
                            line.append(temp[0])
                            temp = [target[i][j]]
                    else:
                        temp = [target[i][j]]
            if temp:
                line.append(temp[0])
            line.extend([0]*(N-len(line)))
            finished.append(line[::-1])
        if finished == target:
            continue
        push(depth+1, next_max, finished)


N = int(input())

board = []
max_num = 0
for i in range(N):
    line = list(map(int, input().split()))
    board.append(line)
    for j in range(N):
        if line[j] > max_num:
            max_num = line[j]
push(0, max_num, board)
print(max_num)
