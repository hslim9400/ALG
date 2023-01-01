

N, M = map(int, input().split())
board = []

for i in range(N):
    board.append(list(map(int, input().split())))
# 2차원 배열에서 큰 값을 골라 누적합
# 현재보다 앞칸들을 확인하기 위해 첫 열과 행은 전처리
for i in range(1, N):
    board[i][0] += board[i-1][0]
for j in range(1, M):
    board[0][j] += board[0][j-1]

for r in range(1, N):
    for c in range(1, M):
        if board[r-1][c] > board[r][c-1]:
            board[r][c] += board[r-1][c]
        else:
            board[r][c] += board[r][c-1]
max_candy = board[N-1][M-1]
print(max_candy)
