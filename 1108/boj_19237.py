import sys
sys.setrecursionlimit(1500)
dr = [0, -1, 1, 0, 0]
dc = [0, 0, 0, -1, 1]


def simulate(sec):
    global shark_dict, board, ans

    if len(shark_dict) == 1:
        ans = sec
        return
    if sec == 1000:
        ans = -1
        return

    for shark in shark_dict.keys():
        r, c = shark_dict[shark][0][0], shark_dict[shark][0][1]
        board[(r, c)][1] = [shark, K]
    for shark in shark_dict.keys():
        r, c = shark_dict[shark][0][0], shark_dict[shark][0][1]
        current_d = shark_dict[shark][0][2]
        for d in shark_dict[shark][1][current_d]:
            nr, nc = r+dr[d], c+dc[d]
            if 0 <= nr < N and 0 <= nc < N:
                if not board[(nr, nc)][1]:
                    shark_dict[shark][0] = (nr, nc, d)
                    board[(nr, nc)][0].add(shark)
                    board[(r, c)][0].discard(shark)
                    break
        else:
            for d in shark_dict[shark][1][current_d]:
                nr, nc = r + dr[d], c + dc[d]
                if 0 <= nr < N and 0 <= nc < N:
                    if board[(nr, nc)][1][0] == shark:
                        shark_dict[shark][0] = (nr, nc, d)
                        board[(nr, nc)][0].add(shark)
                        board[(r, c)][0].discard(shark)
                        break

    for i in range(N):
        for j in range(N):
            if len(board[(i, j)][0]) > 1:
                target = min(board[(i, j)][0])
                for shark in board[(i, j)][0]:
                    if shark == target:
                        continue
                    del shark_dict[shark]
                board[(i, j)][0] = {target}

            if board[(i, j)][1]:
                board[(i, j)][1][1] -= 1
                if not board[(i, j)][1][1]:
                    board[(i, j)][1] = []

    simulate(sec+1)


N, M, K = map(int, input().split())
board = {}
shark_dict = {}
for i in range(N):
    line = list(map(int, input().split()))
    for j in range(N):
        board[(i, j)] = [set(), []]
        if line[j]:
            shark_dict[line[j]] = [(i, j)]
            board[(i, j)] = [{line[j]}, []]

line = list(map(int, input().split()))
for i in range(M):
    shark_dict[i+1] = [(shark_dict[i+1][0][0], shark_dict[i+1][0][1], line[i])]

for i in range(1, M+1):
    shark_dict[i].append({})
    for j in range(4):
        shark_dict[i][1][j+1] = list(map(int, input().split()))
ans = 0
simulate(0)
print(ans)