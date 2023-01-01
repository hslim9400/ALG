

T = int(input())
for test_case in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    board = []
    tunnels = {
        1: [1, 1, 1, 1],
        2: [0, 1, 0, 1],
        3: [1, 0, 1, 0],
        4: [1, 0, 0, 1],
        5: [1, 1, 0, 0],
        6: [0, 1, 1, 0],
        7: [0, 0, 1, 1]
    }
    for i in range(N):
        line = list(map(int, input().split()))
        for j in range(M):
            if line[j] != 0:
                line[j] = tunnels[line[j]]
        board.append(line)

    queue = [((R, C), 0)]
    visited = set()
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    while queue:
        current = queue.pop(0)
        r = current[0][0]
        c = current[0][1]
        dist = current[1]
        if dist == L:
            break
        if (r, c) in visited:
            continue
        visited.add((r,c))
        for d in range(4):
            if 0 <= r+dr[d] < N and 0 <= c+dc[d] < M and board[r][c]:
                if (r+dr[d], c+dc[d]) not in visited:
                    if board[r][c][d]:
                        if board[r+dr[d]][c+dc[d]]:
                            if d == 0:
                                if board[r + dr[d]][c + dc[d]][2]:
                                    queue.append(((r+dr[d], c+dc[d]), dist+1))
                            if d == 1:
                                if board[r + dr[d]][c + dc[d]][3]:
                                    queue.append(((r+dr[d], c+dc[d]), dist+1))
                            if d == 2:
                                if board[r + dr[d]][c + dc[d]][0]:
                                    queue.append(((r+dr[d], c+dc[d]), dist+1))
                            if d == 3:
                                if board[r + dr[d]][c + dc[d]][1]:
                                    queue.append(((r+dr[d], c+dc[d]), dist+1))

    print(f'#{test_case} {len(visited)}')