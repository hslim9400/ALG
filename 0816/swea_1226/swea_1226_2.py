for test_case in range(10):
    # ///////////////////////////////////////////////////////////////////////////////////
    case = int(input())
    maze = []
    start = []
    end = []
    road = []
    prev = []
    cur = []
    ans = 0

    for i in range(16):
        maze.append(list(map(int, list(input()))))

    for i in range(16):
        if 2 in maze[i]:
            start.append([i, maze[i].index(2)])
        if 3 in maze[i]:
            end.append([i, maze[i].index(3)])

    prev = start
    road.append(start[0])

    while prev != []:
        for i in range(len(prev)):
            cur.append([prev[i][0] + 1, prev[i][1]])
            cur.append([prev[i][0], prev[i][1] + 1])
            cur.append([prev[i][0] - 1, prev[i][1]])
            cur.append([prev[i][0], prev[i][1] - 1])
        prev = []
        for i in range(len(cur)):
            if (cur[i][0] or cur[i][1]) == (-1 or 16):
                del cur[i]
            if maze[cur[i][0]][cur[i][1]] == 0:
                road.append([cur[i][0], cur[i][1]])
                prev.append([cur[i][0], cur[i][1]])
                maze[cur[i][0]][cur[i][1]] = 1
            if maze[cur[i][0]][cur[i][1]] == 3:
                ans = 1

        cur = []
        road = list(set(map(tuple, road)))
        prev = list(set(map(tuple, prev)))

    c = '#' + str(test_case + 1) + ' ' + str(ans)

    print(c)