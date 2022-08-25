N = int(input())
K = int(input())
board = [[0]*N for _ in range(N)]
for _ in range(K):
    r, c = map(int, input().split())
    board[r-1][c-1] = 1

board[0][0] = 3
snake = [[[0,0], 0], [[0,0], 0]]
L = int(input())
gts = []
cds = []
for _ in range(L):
    gt, cd = input().split()
    gts.append(int(gt))
    cds.append(cd)
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
d = 0
t = 0

while True:
    dh, dt = snake[0][1], snake[-1][1]
    if 0 <= snake[0][0][0] + dr[d] < N and 0 <= snake[0][0][1] + dc[d] < N or\
            board[snake[0][0][0] + dr[d]][snake[0][0][1] + dc[d]] != 3:

        snake[0][0][0], snake[0][0][1] = snake[0][0][0] + dr[d], snake[0][0][1] + dc[d]

        if board[snake[-1][0][0] + dr[d]][snake[-1][0][1] + dc[d]] == 1:
            continue


    else:
        break

