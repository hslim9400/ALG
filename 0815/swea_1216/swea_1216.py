import sys
sys.stdin = open("input.txt", "r")
T = 10
for test_case in range(1, T + 1):
    tc = int(input())
    board = []
    for _ in range(100):
        board.append(list(input()))  # 문자열을 리스트로 만들어 추가
    trans_board = list(zip(*board))  # 세로 회문을 확인하기 위해 전치

    max_circular = 100
    flag = False
    for k in range(100, -1, -1):
        # 회문의 길이가 99개 인것부터 내려가며 확인
        if flag:
            break
        for i in range(100):
            for j in range(100-k+1):
                # 길이가 k인 회문이 있는지 가로, 세로를 동시에 확인한다.
                if (board[i][j: j+k] == board[i][j: j+k][::-1]) or\
                        (trans_board[i][j: j+k] == trans_board[i][j: j+k][::-1]):
                    max_circular = k
                    flag = True
                    break

    print(f'#{test_case} {max_circular}')
