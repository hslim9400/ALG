T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    board = []
    for _ in range(N):
        board = board + [[0]*N]  # N제곱 크기의 2차원배열 생성

    dx, dy = [0, 1, 0, -1] * N, [1, 0, -1, 0] * N  # 위로 가다가 오른쪽으로 방향전환하기 위해 넉넉히 만들기
    x, y, d, num = 0, 0, 0, 1  # 초기값 설정

    while num != (N**2)+1:
        board[x][y] = num  # 1부터 놓기
        if (0 <= x+dx[d] < N) and (0 <= y+dy[d] < N) and (board[x+dx[d]][y+dy[d]] == 0):
            pass  # 판을 벗어나거나, 다른 숫자를 만날 시 방향전환하기 위한 조건
        else:
            d = d + 1  # 방향전환
        x = x + dx[d]  # 1칸 진행, 숫자 + 1
        y = y + dy[d]
        num = num + 1

    print(f'#{test_case}')
    for i in range(N):  # int로 되어있는 리스트를 모아서 출력하기 위함
        print(' '.join(list(map(str, board[i]))))