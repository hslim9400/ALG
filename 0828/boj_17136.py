def cover_one(r, c, used):
    global board, papers, min_used
    if r == 10:
        if used < min_used:
            min_used = used
        return

    if c == 10:
        cover_one(r+1, 0, used)
        return

    if board[r][c] == 0:
        cover_one(r, c+1, used)
        return

    for size in range(1, 6):
        if papers[size] == 0:
            continue
        if r+size >= 11 or c+size >= 11:
            continue
        flag = False
        for i in range(size):
            for j in range(size):
                if board[r+i][c+j] == 0:
                    flag = True
                    break
            if flag:
                break
        else:
            used += 1
            papers[size] -= 1
            for i in range(size):
                for j in range(size):
                    board[r+i][c+j] = 0
            cover_one(r, c+size, used)
            used -= 1
            papers[size] += 1
            for i in range(size):
                for j in range(size):
                    board[r+i][c+j] = 1


papers = {1: 5, 2: 5, 3: 5, 4: 5, 5: 5}
board = []
ones = 0
for _ in range(10):
    line = list(map(int, input().split()))
    board.append(line)
    ones += line.count(1)
min_used = 25
cover_one(0, 0, 0)

if min_used == 25:
    ans = -1
else:
    ans = min_used
print(ans)

