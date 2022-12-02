# 사용한 자료구조
# dusts: 좌표를 키, 먼지의 크기를 값으로 갖는 딕셔너리
# robot: [위쪽 로봇 좌표, 아래쪽 로봇 좌표]로 구성된 리스트

# 편의를 위해 위쪽 델타탐색과 아래쪽 델타탐색을 다른 순서로 구성
dr_upper = [-1, 0, 1, 0]
dc_upper = [0, 1, 0, -1]
dr_downer = [1, 0, -1, 0]
dc_downer = [0, 1, 0, -1]

# 먼지가 확산되는 함수
# 먼저 확산된 먼지가 다음 먼지의 확산에 영향을 주면 안되므로 새로운 딕셔너리를 만들어 넣는다.
def diffusion():
    global dusts
    new_dusts = {}
    for dust in dusts.keys():
        diffused = 0
        r, c = dust
        if not dusts[dust]:
            if dust not in new_dusts.keys():
                new_dusts[dust] = 0
                continue
            continue

        for d in range(4):
            nr, nc = r+dr_upper[d], c+dc_upper[d]
            if 0 <= nr < R and 0 <= nc < C and (nr, nc) not in robot:
                if (nr, nc) in new_dusts.keys():
                    new_dusts[(nr, nc)] += dusts[dust] // 5
                    diffused += 1
                else:
                    new_dusts[(nr, nc)] = dusts[dust] // 5
                    diffused += 1
        if dust in new_dusts.keys():
            new_dusts[dust] += dusts[dust] - (dusts[dust] // 5) * diffused
        else:
            new_dusts[dust] = dusts[dust] - (dusts[dust] // 5) * diffused

    dusts = new_dusts


# 공기청정기를 돌리는 함수
# 문제와 같이 먼지를 밀어내기보다는 반대로 돌며 당겨오는 것이 구현하기 쉽다.
def clean():
    global dusts

    for start in robot:
        upper = 1 - robot.index(start)
        # 위쪽 로봇이면 upper가 1, 아래쪽이면 0
        # 이에 따라 위에서 나눠놓은 델타탐색 리스트가 결정됨
        if upper:
            dr, dc = dr_upper, dc_upper
        else:
            dr, dc = dr_downer, dc_downer
        prev = start[0] + dr[0], start[1] + dc[0]
        for d in range(4):
            while True:
                nr, nc = prev[0] + dr[d], prev[1] + dc[d]
                if (nr, nc) == start:
                    dusts[prev] = 0
                    break
                if d < 3 and nr == start[0]+dr[d]:
                    break
                if 0 <= nr < R and 0 <= nc < C:
                    dusts[prev] = dusts[(nr, nc)]
                    prev = (nr, nc)
                else:
                    break


R, C, T = map(int, input().split())
robot = [0, 0]
dusts = {}

for i in range(R):
    line = list(map(int, input().split()))
    for j in range(C):
        if line[j] == -1:
            if not robot[0]:
                robot[0] = (i, j)
            else:
                robot[1] = (i, j)
        elif line[j]:
            dusts[(i, j)] = line[j]
        else:
            dusts[(i, j)] = 0
for t in range(T):
    diffusion()
    clean()
ans = 0
for dust in dusts:
    ans += dusts[dust]
print(ans)

