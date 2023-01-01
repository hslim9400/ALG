n, m = map(int, input().split())
board = []
for i in range(n):
    line = list(map(int, list(input())))
    board.append(line)

ans = 0
for r in range(n):
    if board[r][0]:
        ans = 1
for c in range(m):
    if board[0][c]:
        ans = 1

for r in range(1, n):
    for c in range(1, m):
        if board[r][c]:
            if ans == 0:
                ans = 1
            if board[r-1][c-1]:
                length = 0
                for k in range(1, board[r-1][c-1]+1):
                    if board[r-k][c] * board[r][c-k] == 0:
                        break
                    length += 1
                board[r][c] = length + 1
                if ans < board[r][c]:
                    ans = board[r][c]


print(ans*ans)
