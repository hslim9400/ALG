def one_area(i, j):
    global survived, visited

    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    queue = [(i, j)]
    sheep = 0
    wolf = 0
    while queue:  # bfs
        current = queue.pop(0)
        if visited[current[0]][current[1]]:
            continue
        visited[current[0]][current[1]] = 1
        if garden[current[0]][current[1]] == 'o':  # 양을 센다
            sheep += 1
        if garden[current[0]][current[1]] == 'v':  # 늑대를 센다
            wolf += 1
        next_steps = []
        for d in range(4):
            if 0 <= current[0] + dr[d] < r and 0 <= current[1] + dc[d] < c:
                if garden[current[0]+dr[d]][current[1]+dc[d]] != '#' and \
                        not visited[current[0]+dr[d]][current[1]+dc[d]]:  # 벽이 아니면 확인
                    next_steps.append((current[0]+dr[d], current[1]+dc[d]))
        for next_step in next_steps:
            if next_step not in queue:
                queue.append(next_step)
    if sheep > wolf:  # 양이 많다면
        survived[0] += sheep  # 양 승
    else:  # 늑대가 많다면
        survived[1] += wolf  # 늑대 승
    return


r, c = map(int, input().split())
areas = [[]]
garden = []
for i in range(r):
    line = list(input())
    garden.append(line)

visited = [[0]*c for _ in range(r)]  # 포문 안에서 bfs함수를 동작시킬것이므로 글로벌에서 비지티드를 만든다.
survived = [0, 0]
for i in range(r):
    for j in range(c):
        if garden[i][j] != '#' and not visited[i][j]:  # 처음 가보는 구역이면 bfs
            one_area(i, j)

print(*survived)

