def make_path(top):
    global max_path
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    # 좌표와 그 좌표까지의 등산로의 길이를 함께 저장
    queue = [(top, 1)] # 시작칸을 포함해서 등산로의 길이가 된다.
    path_len = 1
    while queue: # bfs로 등산로 찾기
        current = queue.pop(0)
        r = current[0][0]
        c = current[0][1]
        path_len = current[1]
        for d in range(4):
            if 0 <= r+dr[d] < N and 0 <= c+dc[d] < N:
                # 문제의 조건. 현재보다 높이가 낮은 칸으로만 등산로를 조성할 수 있다.
                if board[r+dr[d]][c+dc[d]] < board[r][c]:
                    queue.append(((r+dr[d], c+dc[d]), path_len+1))
    if path_len > max_path: # 최대 등산로 길이를 갱신
        max_path = path_len


T = int(input())
for test_case in range(1, T+1):
    N, K = map(int, input().split())
    board = []
    tops = []
    top = 0
    for i in range(N):
        line = list(map(int, input().split()))
        board.append(line)
        # 한 줄 한 줄 받으며 봉우리를 찾는다.
        for j in range(N):
            if line[j] > top:
                # 기존 봉우리보다 높은 봉우리를 찾았다면 봉우리들을 초기화
                top = line[j]
                tops = []
                tops.append((i, j))
            elif line[j] == top:
                # 기존 봉우리와 같은 높이의 봉우리를 찾으면 추가
                tops.append((i, j))

    max_path = 0
    # 모든 공사의 경우에 대해 완전탐색
    for i in range(N):
        for j in range(N):
            for k in range(1, K+1):
                board[i][j] -= k
                if board[i][j] == -1:
                    # 한 칸만 깎을 수 있으므로 0까지만 확인하면 됨
                    board[i][j] += k
                    break
                for top in tops:
                    # 봉우리를 깎았다면 그 녀석은 봉우리가 아니다.
                    if top == (i, j):
                        continue
                    # 등산로를 찾아줌
                    make_path(top)
                # 깎은것은 다시 채워놓는다.
                board[i][j] += k
    print(f'#{test_case} {max_path}')