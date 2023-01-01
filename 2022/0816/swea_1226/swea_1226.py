import sys
sys.stdin = open("input.txt", "r")

T = 10
for test_case in range(1, T+1):
    tc = input()
    maze = []
    road = []
    for i in range(16):
        line = list(map(int, list(input())))
        maze.append(line)
        for j in range(16):
            if line[j] == 2:
                start = [i, j]
            if line[j] == 3:
                end = [i, j]

    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]
    stack = [start]
    visited = []
    while stack:
        current = stack.pop()
        if current not in visited:
            visited.append(current)
        next_steps = []
        for i in range(4):
            if maze[current[0]+dr[i]][current[1] + dc[i]] != 1:
                next_steps.append([current[0]+dr[i], current[1] + dc[i]])

        for next_step in next_steps:
            if next_step not in visited:
                stack.append(next_step)

    ans = 0
    if end in visited:
        ans = 1
    print(f'#{test_case} {ans}')
