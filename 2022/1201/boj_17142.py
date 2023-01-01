from itertools import combinations
from copy import deepcopy
# 사용한 자료구조
# board: 연구소. 원본인 original_board를 복사해 매 시행 때 current_board로 사용
# 빈 공간 = 0, 벽 = 1, 비활성 바이러스 = 2, 활성 바이러스 = -2
# viruses: 바이러스들의 좌표가 들어있는 set
# left: 남은 빈 공간 수
# starts: 시작 가능한 좌표들로 부터 M개를 추출한 조합을 모아놓은 리스트
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


# 1초동안 바이러스가 확산되는 함수
# 비활성 바이러스(-2)는 여기로 확산이 닿아도 left를 줄이지 않는 점에서 빈 공간(0)과 구분되어야 하고
# 활성 바이러스가 닿을 경우 다음 확산을 이어간다는 점에서 활성바이러스(2)와 구분되어야 한다.
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
        if ans == time:
            break
        time += 1
        viruses = simulate(viruses)
    if left:  # 모든 공간을 바이러스로 채워야 답을 갱신할 수 있다.
        continue
    ans = min(ans, time)

if ans == N * N:
    ans = -1
print(ans)