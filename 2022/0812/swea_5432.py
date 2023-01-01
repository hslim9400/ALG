T = int(input())
for test_case in range(1, T + 1):

    board = input()
    steels = [0]  # 끝나지 않은 쇠막대기들
    cut_steels = []  # 끝난 쇠막대기들
    for i in range(len(board)):
        if board[i] == '(':
            if board[i + 1] != ')':  # 레이저가 아니라면 쇠막대기 이므로 쇠막대기 추가
                steels.append(1)
            else:
                for j in range(len(steels)):  # 레이저라면 현재 있는 끝나지 않은 쇠막대기를 모두 자름
                    steels[j] = steels[j] + 1
        else:
            if board[i - 1] == '(':  # 레이저는 이미 반영함
                pass
            else:  # 레이저가 아니라면 쇠막대기가 끝났으므로 가장 뒤의 쇠막대기를 뽑아낸다
                cut_steels.append(steels.pop())
    print(f'#{test_case} {sum(cut_steels)}')  # 조각난 쇠막대기들의 총합
