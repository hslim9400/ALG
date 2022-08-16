T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    board = []
    for _ in range(N):
        board.append(list(input()))
    trans_board = list(zip(*board))  # 세로 회문을 확인하기 위해 전치
    ans = 0
    for i in range(N):
        for j in range(N-M+1):  # 길이가 M이 되는 문자열들을 확인
            if board[i][j:j+M] == board[i][j:j+M][::-1]:  # 회문 확인, 뒤집어도 같은 단어가 된다
                ans = board[i][j:j+M]
            if trans_board[i][j:j+M] == trans_board[i][j:j+M][::-1]:
                ans = trans_board[i][j:j+M]
    print(f'#{test_case} {ans}')
