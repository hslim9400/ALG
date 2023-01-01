def make_move(board, r, c, color):  # 명령을 수행하는 함수
    board[r][c] = color
    for i in range(3):  # dr과 dc를 조합해 여덟방향을 모두 확인한다.
        for j in range(3):
            if i == 0 and j == 0:  # (0, 0)은 움직이지 않으므로 건너뜀
                continue
            check = 1
            # 내가 둔 돌 - 확인하는 방향을 진행하며 반대 색의 돌이 몇개 나오는지 세고 같은 색이 등장하면 종료한다. 세준만큼 다시 진행하며 내 색의 돌로 바꾼다.
            # 빈 칸이 나오면 이 방향은 버린다.
            while True:
                if (0 <= r + check*dr[i] < N) and (0 <= c + check*dc[j] < N):
                    if board[r + check * dr[i]][c + check * dc[j]] == 0:
                        break
                    elif board[r + check*dr[i]][c + check*dc[j]] != color:  # 다른 색이므로 카운트 증가
                        check += 1
                    else:  # 같은 색을 발견
                        for ch in range(1, check):  # 카운트 한 만큼
                            board[r + ch*dr[i]][c + ch*dc[j]] = color  # 내 색으로 바꾼다.
                        break
                else:
                    break
    return board


T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    board = [[0]*N for _ in range(N)]
    # 보드 중앙의 색을 바꾼다.
    board[N//2][N//2], board[N//2-1][N//2-1] = 2, 2
    board[N//2][N//2-1], board[N//2-1][N//2] = 1, 1
    # 대각선을 포함해 여덟개의 방향을 확인 할 예정
    dr = [0, 1, -1]
    dc = [0, 1, -1]

    for k in range(M):  # 입력받은 명령을 수행
        c, r, color = map(int, input().split())  # 가로축을 먼저 입력받으므로 c, r로 받음
        r, c = r - 1, c - 1  # 입력은 1부터 N범위
        board = make_move(board, r, c, color)

    white = 0
    black = 0
    for i in range(N):
        white += board[i].count(2)
        black += board[i].count(1)
    print(f'#{test_case} {black} {white}')