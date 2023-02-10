def solution(game_board, table):
    answer = 0
    possible_peices = {}
    real_spaces = set()
    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]
    N = len(game_board)

    def find_peices(board):
        visited = set()
        peices = {}

        for i in range(N):
            for j in range(N):
                if board[i][j] and (i, j) not in visited:
                    stack = [(i, j)]
                    peice = []
                    while stack:
                        r, c = stack.pop()
                        if (r, c) in visited:
                            continue
                        peice.append((i-r, j-c))
                        visited.add((r, c))
                        for d in range(4):
                            if 0 <= r+dr[d] < N and 0 <= c+dc[d] < N and \
                                    board[r+dr[d]][c+dc[d]] and (r+dr[d], c+dc[d]) not in visited:
                                stack.append((r+dr[d], c+dc[d]))
                    peice = tuple(peice)
                    if peice in peices.keys():
                        peices[peice] += 1
                    else:
                        possible_peices[peice] = 1

        print(peices)
        return peices

    real_spaces = find_peices(game_board)
    new_peices = find_peices(table)
    for peice in new_peices.keys():
        if peice in possible_peices.keys():
            possible_peices[peice] += new_peices[peice]
        else:
            possible_peices[peice] = new_peices[peice]
    table = list(zip(*table[::-1]))
    new_peices = find_peices(table)
    for peice in new_peices.keys():
        if peice in possible_peices.keys():
            possible_peices[peice] += new_peices[peice]
        else:
            possible_peices[peice] = new_peices[peice]
    table = list(zip(*table[::-1]))
    new_peices = find_peices(table)
    for peice in new_peices.keys():
        if peice in possible_peices.keys():
            possible_peices[peice] += new_peices[peice]
        else:
            possible_peices[peice] = new_peices[peice]
    table = list(zip(*table[::-1]))
    new_peices = find_peices(table)
    for peice in new_peices.keys():
        if peice in possible_peices.keys():
            possible_peices[peice] += new_peices[peice]
        else:
            possible_peices[peice] = new_peices[peice]

    print()
    print(possible_peices)
    for peice in real_spaces:
        if peice in possible_peices:
            answer += len(peice) * min(real_spaces[peice], possible_peices[peice])

    print(answer)
    return answer

solution([[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]],
         [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]])
