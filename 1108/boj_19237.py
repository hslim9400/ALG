import sys
sys.setrecursionlimit(1500)
dr = [0, -1, 1, 0, 0]
dc = [0, 0, 0, -1, 1]
# 사용한 자료구조:
# shark_dict : {상어의 번호: [좌표, 상어가 바라보는 방향:상어가 선호하는 방향리스트]} 인 딕셔너리
# board : {가상좌표: [{좌표에 있는 상어set}, [좌표에 있는 상어 냄새, 남은 시간]]} 인 딕셔너리


# 1초에 벌어지는 일을 구현한 재귀함수
# 상어가 한마리 남거나, 시간이 1000초가 되면 종료 
def simulate(sec):
    global shark_dict, board, ans

    if len(shark_dict) == 1:
        ans = sec
        return
    if sec == 1000:
        ans = -1
        return

    # 모든 상어들이 먼저 냄새를 뿌린 후 이동을 시작한다.
    # 상어들을 한 번만 순회하며 냄새를 뿌림과 동시에 이동하면 오답
    for shark in shark_dict.keys():
        r, c = shark_dict[shark][0][0], shark_dict[shark][0][1]
        board[(r, c)][1] = [shark, K]
    for shark in shark_dict.keys():
        r, c = shark_dict[shark][0][0], shark_dict[shark][0][1]
        current_d = shark_dict[shark][0][2]
        for d in shark_dict[shark][1][current_d]:
            # for-else구문으로 냄새가 없는 자리가 없을 경우 본인이 남긴 냄새가 있는 자리로 가도록 함
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
            # 모든 좌표를 순회하며 겹치는 상어를 없애주고
            # 냄새가 남은 시간을 감소시키다.
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