from itertools import combinations
from copy import deepcopy
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def simulate(viruses):
    global current_board, left
    new_virus = set()
    for virus in viruses:
        r, c = virus
        for d in range(4):
            nr, nc = r + dr[d], c+ dc[d]
            if 0 <= nr < N and 0 <= nc < N and current_board[nr][nc] != 1 and current_board[nr][nc] != -2:
                if not current_board[nr][nc]:
                    new_virus.add((nr, nc))
                    current_board[nr][nc] = -2
                    left -= 1
                    if not left:
                        return 0
                else:
                    new_virus.add((nr, nc))
                    current_board[nr][nc] = -2

    return new_virus


N, M = map(int, input().split())
original_board = []
virus_spots = set()
original_left = N * N
for i in range(N):
    line = list(map(int, input().split()))
    original_board.append(line)
    for j in range(N):
        if line[j] == 2:
            virus_spots.add((i, j))
            original_left -= 1
        if line[j] == 1:
            original_left -= 1

starts = list(combinations(virus_spots, M))
ans = N*N
for start in starts:
    time = 0
    left = original_left
    if not left:
        ans = 0
        break
    current_board = deepcopy(original_board)
    viruses = set(start)
    for virus in viruses:
        current_board[virus[0]][virus[1]] = -2
    while viruses:
        time += 1
        viruses = simulate(viruses)
    if left:
        continue
    ans = min(ans, time)

if ans == N * N:
    ans = -1
print(ans)