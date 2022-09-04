def one_area(i, j):
    global survived, visited

    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    queue = [(i, j)]
    sheep = 0
    wolf = 0
    while queue:
        current = queue.pop(0)
        if visited[current[0]][current[1]]:
            continue
        visited[current[0]][current[1]] = 1
        if garden[current[0]][current[1]] == 'o':
            sheep += 1
        if garden[current[0]][current[1]] == 'v':
            wolf += 1
        next_steps = []
        for d in range(4):
            if 0 <= current[0] + dr[d] < r and 0 <= current[1] + dc[d] < c:
                if garden[current[0]+dr[d]][current[1]+dc[d]] != '#' and \
                        not visited[current[0]+dr[d]][current[1]+dc[d]]:
                    next_steps.append((current[0]+dr[d], current[1]+dc[d]))
        for next_step in next_steps:
            if next_step not in queue:
                queue.append(next_step)
    if sheep > wolf:
        survived[0] += sheep
    else:
        survived[1] += wolf
    return


r, c = map(int, input().split())
areas = [[]]
garden = []
for i in range(r):
    line = list(input())
    garden.append(line)

visited = [[0]*c for _ in range(r)]
survived = [0, 0]
for i in range(r):
    for j in range(c):
        if garden[i][j] != '#' and not visited[i][j]:
            one_area(i, j)

print(*survived)

