# 일단 가장 좌상단에 쓰레기위치에 로봇을 배치
# 로봇이 쓰레기를 순회하며 수거가능한 쓰레기를 수거, 수거하며 현위치를 변경
# 쓰레기는 행, 열로 정렬되어 있으므로 문제 조건대로 수거하게 됨
# 쓰레기를 다시 돌며 수거하지 않은 쓰레기 중 가장 좌상단에 로봇을 배치, 이하 반복


N, M = map(int, input().split())
board = []
trashes = []
for i in range(N):
    line = list(map(int, input().split()))
    for j in range(M):
        if line[j]:
            trashes.append([i, j, 0])
left = len(trashes)
start = 0
current = 0
robots = 0
while left:
    robots += 1
    for start_idx in range(start, len(trashes)):
        if not trashes[start_idx][2]:
            current = start_idx
            trashes[start_idx][2] = 1
            left -= 1
            start = start_idx + 1
            break
    for trash_idx in range(start, len(trashes)):
        if not trashes[trash_idx][2] and \
                trashes[trash_idx][0] >= trashes[current][0] and trashes[trash_idx][1] >= trashes[current][1]:
            current = trash_idx
            trashes[trash_idx][2] = 1
            left -= 1
print(robots)