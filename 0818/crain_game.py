def solution(board, moves):
    stack = []
    count = 0
    board = list(map(list, zip(*board)))
    while moves:
        current = moves.pop(0) - 1
        for i in (range(len(board))):
            if board[current][i] != 0:
                doll = board[current][i]
                board[current][i] = 0
                break
        else:
            continue
        if stack:
            if stack[-1] == doll:
                stack.pop()
                count += 2
            else:
                stack.append(doll)
        else:
            stack.append(doll)
    answer = count
    return answer


print(solution([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]], [1, 5, 3, 5, 1, 2, 1, 4]))