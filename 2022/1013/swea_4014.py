def check_line(line):  # 해당 행을 체크하는 함수
    for i in range(N):
        line[i] = [line[i], False]  # 다리를 놓았는지 여부를 같이 기록해놓음
    for i in range(1, N):  # 종료조건들을 마구 놓고 조건 충족 시 0을 반환
        if abs(line[i][0] - line[i-1][0]) > 1:  # 높이차이가 1보다 크면 이미 불가능
            return 0
        if line[i][0] == line[i-1][0] - 1:  # 내 앞의 높이와 비교해 내가 낮을 경우 내 뒤로 다리를 놓아준다.
            for k in range(X):
                if i+k == N:  # 벗어남
                    return 0
                if line[i+k][1]:  # 이미 다리 있음
                    return 0
                if line[i+k][0] != line[i][0]:  # 높이가 달라 다리를 놓지 못함
                    return 0
                line[i+k][1] = True  # 다리를 놓아준다.

        if line[i][0] == line[i-1][0] + 1:  # 내가 높다면 앞으로 다리를 놓는다.
            for k in range(X):
                if i-1-k == -1:
                    return 0
                if line[i-1-k][1]:
                    return 0
                if line[i-1-k][0] != line[i-1][0]:
                    return 0
                line[i-1-k][1] = True
    return 1  # 어쨌거나 한 행을 모두 지나왔다면 1점


T = int(input())
for test_case in range(1, T+1):
    N, X = map(int, input().split())
    board = []
    for i in range(N):
        board.append(list(map(int, input().split())))

    trans_board = list(map(list, zip(*board)))  # 세로를 확인하기 위해 전치

    ans = 0
    for i in range(N):  # 모든 행, 전치 행에 대해 시행하며 가능한 행이라면 1이 반환되어 답에 더해준다.
        ans += check_line(board[i])
        ans += check_line((trans_board[i]))

    print(f'#{test_case} {ans}')
