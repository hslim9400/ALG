def move(time, colonies):
    global alive
    if time == M:
        alive = 0
        for colony in colonies:
            alive += colonies[colony][0]
        return

    new_colonies = {}
    dr = [-1, 0, 0, 1]
    dc = [0, 1, -1, 0]

    for colony in colonies.keys():
        r, c = colony
        d = colonies[colony][1]
        n = colonies[colony][0]
        if not n:
            continue
        r, c = r+dr[d], c+dc[d]
        if (r, c) not in new_colonies.keys():
            new_colonies[(r, c)] = [n, d]
        else:
            new_colonies[(r, c)].extend([n, d])
        if r == 0 or r == N-1 or c == 0 or c == N-1:
            new_colonies[(r, c)][0] //= 2
            new_colonies[(r, c)][1] = 3 - d

    for colony in new_colonies.keys():
        if len(new_colonies[colony]) > 2:
            max_num = new_colonies[colony][0]
            num = 0
            d = new_colonies[colony][1]
            for i in range(len(new_colonies[colony])//2):
                if new_colonies[colony][2*i] > max_num:
                    max_num = new_colonies[colony][2*i]
                    d = new_colonies[colony][2*i + 1]
                num += new_colonies[colony][2*i]
            new_colonies[colony] = [num, d]

    move(time+1, new_colonies)


T = int(input())
for test_case in range(1, T+1):
    N, M, K = map(int, input().split())

    directions = {1: 0, 2: 3, 3: 2, 4: 1}
    colonies = {}
    for i in range(K):
        r, c, n, d = map(int, input().split())
        colonies[(r,c)] = [n, directions[d]]

    alive = 10000 * K
    move(0, colonies)
    print(f'#{test_case} {alive}')