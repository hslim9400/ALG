def cycle(start_r, start_c, side_1, side_2):
    # 정해진 경로를 따라 카페투어
    r = start_r
    c = start_c
    cafes = set()  # 같은 디저트를 팔면 종료 할 것이므로
    cafes.add(board[r][c])
    counts = 1  # 시작과 동시에 카페를 한군데는 갔다.
    for i in range(side_1):  # 왼쪽 아래방향
        r += 1
        c -= 1
        cafes.add(board[r][c])
        counts += 1
        if len(cafes) != counts:
            return -1

    for i in range(side_2):  # 오른쪽 아래방향
        r += 1
        c += 1
        cafes.add(board[r][c])
        counts += 1
        if len(cafes) != counts:
            return -1

    for i in range(side_1):  # 오른쪽 위 방향
        r -= 1
        c += 1
        cafes.add(board[r][c])
        counts += 1
        if len(cafes) != counts:
            return -1

    for i in range(side_2-1):  # 왼쪽 위 방향
        # 마지막에 원위치로 돌아오면 안됨
        r -= 1
        c -= 1
        cafes.add(board[r][c])
        counts += 1
        if len(cafes) != counts:
            return -1
    return counts


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    board = []
    for _ in range(N):
        board.append(list(map(int, input().split())))

    max_cafes = -1
    for start_r in range(N-2):  # 시작 가능한 r과 c를 모두 탐색
        for start_c in range(1, N-1):
            for side_1 in range(1, min(start_c, N-2-start_r)+1):
                # 시작점에 따라 왼쪽아래로 뻗을 수 있는 대각선의 최댓값이 정해짐
                for side_2 in range(1, min(N-1-start_c, N-1-side_1-start_r)+1):
                    # 시작점과 첫 대각선의 길이에 따라 오른쪽 아래로 가거나
                    # 세 번째 지점에서 돌아오는 대각선의 최댓값이 정해짐
                    # 시작점과 두 대각선이 정해졌다면 경로 한 개가 완성됨
                    visited = cycle(start_r, start_c, side_1, side_2)
                    if visited > max_cafes:  # 투어 결과 카페를 많이 갔다면 갱신
                        max_cafes = visited

    print(f'#{test_case} {max_cafes}')
