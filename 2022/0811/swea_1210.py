
for test_case in range(1, 11):
    tc = int(input())
    board = []
    for _ in range(100):
        board.append(list(map(int, input().split())))
    for i in range(100):
        if board[99][i] == 2:  # 목표 도착점을 먼저 찾는다
            c = i
    r = 99  # 목표점부터 거슬러 올라갈 것

    while r > 0:  # 출발 행에 도착하면 종료
        r = r - 1  # 한칸 올라간다.
        if 0 < c < 100:  # 1부터 99, 왼쪽을 볼거기 때문
            if board[r][c - 1] == 1:  # 길이 있다면
                while True:  # 길 끝까지 간다.
                    c = c - 1
                    if c == 0:
                        break
                    elif board[r][c - 1] == 0:
                        break
                continue  # 왼쪽으로 갔다면 오른쪽을 확인하면 안된다.

        if 0 <= c < 99:  # 0부터 98, 오른쪽에 길이 있는지 확인한다.
            if board[r][c + 1] == 1:
                while True:
                    c = c + 1
                    if c == 99:
                        break
                    elif board[r][c + 1] == 0:
                        break

    print(f'#{test_case} {c}')