dr_upper = [-1, 0, 1, 0]
dc_upper = [0, 1, 0, -1]
dr_downer = [1, 0, -1, 0]
dc_downer = [0, 1, 0, -1]


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


def clean():
    global dusts

    for start in robot:
        upper = 1 - robot.index(start)
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
board = []
robot = [0, 0]
dusts = {}

for i in range(R):
    line = list(map(int, input().split()))
    board.append(line)
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

