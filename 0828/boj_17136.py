def cover_one(ones, used):
    global board, papers, min_used
    if ones == 0:
        print(used)
        if used < min_used:
            min_used = used
        return

    for i in range(10):
        for j in range(10):
            if board[i][j] == 1:
                for size in range(1, 6):
                    if i+size < 10 and j+size < 10 and papers[size] != 0:
                        flag = False
                        for i_check in range(size):
                            for j_check in range(size):
                                if board[i+i_check][j+j_check] == 0:
                                    flag = True
                                    break
                            if flag:
                                break
                        else:
                            used += 1
                            if used >= min_used:
                                used -= 1
                                return
                            papers[size] -= 1
                            ones -= size**2
                            for i_check in range(size):
                                for j_check in range(size):
                                    board[i+i_check][j+j_check] = 0
                            cover_one(ones, used)
                            used -= 1
                            papers[size] += 1
                            ones += size**2
                            for i_check in range(size):
                                for j_check in range(size):
                                    board[i+i_check][j+j_check] = 1


papers = {1: 5, 2: 5, 3: 5, 4: 5, 5: 5}
board = []
ones = 0
for _ in range(10):
    line = list(map(int, input().split()))
    board.append(line)
    ones += line.count(1)
min_used = 25
cover_one(ones, 0)

if min_used == 25:
    ans = -1
else:
    ans = min_used
print(ans)

