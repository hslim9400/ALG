T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    board = []
    for _ in range(100):
        board.append(list(map(int, input().split())))

    ans = 0
    for c in range(100):  # 큰 자석은 위아래에 배치되어 있으므로
        flag = True
        for r in range(100):  # 같은 열에 대해서 행들을 확인해준다.
            if board[r][c] == 1:  # N극 자석이 있다면
                flag = False  # 기억해뒀다가
            if board[r][c] == 2:  # S극 자석을 발견시
                if not flag:  # N극 자석을 위에서 발견했었다면
                    ans = ans + 1  # 교착상태 + 1
                    flag = True  # 그 아래에선 S극 자석을 발견해도 교착상태가 늘어나지 않음

    print(f'#{test_case} {ans}')