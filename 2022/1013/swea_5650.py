dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def play(start_r, start_c, start_d):  # 시뮬레이션하며 점수 계산
    r, c, d = start_r, start_c, start_d
    point = 0
    while True:
        r += dr[d]  # 먼저 움직이고
        c += dc[d]
        if board[r][c]:  # 구조물을 만났다면 해당 구조물에 맞는 동작을 함
            if board[r][c] == -1:  # 블랙홀
                return point
            if board[r][c] > 5:  # 웜홀
                idx = structures[board[r][c]].index((r, c))  # 어떤 웜홀이 [좌표1, 좌표2]로 저장되어있음.
                r, c = structures[board[r][c]][1-idx]  # 좌표에 맞는 인덱스를 찾아 1에서 빼주면 다른 웜홀
                continue
            d = structures[board[r][c]][d]  # 1,2,3,4,5라면 방향이 변함
            point += 1
        if r == start_r and c == start_c:  # 출발지점에 왔다면 종료
            return point


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    board = []
    # 구조물들, 인덱스에 맞는 딕셔너리이며 웜홀은 좌표를 두개 저장 할 리스트가 될 것
    structures = [
        0,
        {0: 2, 3: 1, 1: 0, 2: 3},
        {0: 2, 1: 3, 2: 1, 3: 0},
        {2: 0, 1: 3, 0: 1, 3: 2},
        {3: 1, 2: 0, 0: 3, 1: 2},
        {1: 3, 3: 1, 0: 2, 2: 0},
        [], [], [], [], []
    ]
    for i in range(N):
        line = [5] + list(map(int, input().split())) + [5]
        for j in range(N+2):
            if line[j] > 5:
                structures[line[j]].append((i+1, j))
        board.append(line)
    board = [[5]*(N+2)] + board +[[5]*(N+2)]

    max_point = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            # N*N*4 완전 탐색
            if not board[i][j]:
                for d in range(4):
                    point = play(i, j, d)  # 출발점, 방향을 선택했을 때 점수
                    if point > max_point:
                        max_point = point

    print(f'#{test_case} {max_point}')
