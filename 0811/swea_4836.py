T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    board = [[0]*10 for _ in range(10)]

    for _ in range(N):  # 사각형마다 시행
        r1, c1, r2, c2, color = list(map(int, input().split()))  # 꼭지점과 색을 받는다.
        for r in range(r1, r2+1):  # 꼭지점이 r2라면 r2를 포함해야 하므로
            for c in range(c1, c2+1):
                if board[r][c] != color:  # 같은 색이 칠해져 있다면 덧칠하지 않는다.
                    board[r][c] = board[r][c] + color  # 그게 아니라면 칠한다.

    ans = 0
    for i in range(10):
        for j in range(10):  # 모든 칸을 확인
            if board[i][j] > 2:  # 같은 색만으로는 덧칠하지 않았기 때문에 3이상이라면 두 색을 모두 칠했다.
                ans = ans + 1

    print(f'#{test_case} {ans}')
