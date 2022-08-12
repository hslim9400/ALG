T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    board = []
    for _ in range(N):
        board.append(list(map(int, input().split())))
    rows = [[]]

    for i in range(N):
        for j in range(N):
            if board[i][j] != 0:
                for k in range(len(rows)):
                    if (i, j-1) in rows[k]:
                        rows[k].append((i, j))
                        break
                else:
                    rows.append([(i, j)])

    recs = [[0, 0]]
    for i in range(len(rows)):
        for j in range(len(recs)):
            if len(rows[i]) == recs[j][0]:
                recs[j][1] = recs[j][1] + 1
                break
        else:
            recs.append([len(rows[i]), 1])

    recs = recs[1:]
    recs.sort(key=lambda x: (x[0] * x[1], x[1]))
    for i in range(len(recs)):
        recs[i][0], recs[i][1] = recs[i][1], recs[i][0]

    ans = []
    for i in range(len(recs)):
        ans.extend(recs[i])

    print(f'#{test_case}',len(recs), *ans)

