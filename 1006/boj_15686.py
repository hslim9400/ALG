N, M = map(int, input().split())
board = []
homes = []
chickens = []
for i in range(N):
    line = list(map(int, input().split()))
    board.append(line)
    for j in range(N):
        if line[j] == 1:
            homes.append((i, j))
        if line[j] == 2:
            chickens.append((i, j))

c = len(chickens)
min_dists = 4*N*N
for i in range(1<<c):
    dists = 0
    if bin(i).count('1') > M:
        continue
    for home in homes:
        dist = 2*N
        for j in range(c):
            if i & (1<<j):
                chicken = chickens[j]
                dist = min(dist, abs(home[0]-chicken[0]) + abs(home[1]-chicken[1]))
        dists += dist
    min_dists = min(dists, min_dists)

print(min_dists)