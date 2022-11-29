dr = [0, -1, 1, 0, 0]
dc = [0, 0, 0, 1, -1]


def move_shark():
    global sharks
    new_sharks = {}
    for shark in sharks.keys():
        r, c = shark
        move_left = sharks[shark][2]
        d = sharks[shark][1]
        while move_left:
            nr, nc = r+dr[d]*move_left, c+dc[d]*move_left
            nd = 0
            if 0 > nr or R <= nr \
                    or 0 > nc or C <= nc:
                if d % 2:
                    if d == 1:
                        moved = r
                    if d == 3:
                        moved = C - 1 - c
                    nd = d + 1
                else:
                    if d == 2:
                        moved = R - 1 - r
                    if d == 4:
                        moved = c
                    nd = d - 1
            else:
                moved = move_left
            if not moved:
                d = nd
                continue
            move_left -= moved
            r, c = r + dr[d]*moved, c + dc[d]*moved
            if nd:
                d = nd
        sharks[shark][1] = d

        if (r, c) in new_sharks.keys():
            new_sharks[(r, c)] = max(new_sharks[(r, c)], sharks[shark])
        else:
            new_sharks[(r, c)] = sharks[shark]
    sharks = new_sharks


def catch_shark(col):
    global sharks, ans
    for r in range(R):
        if (r, col) in sharks.keys():
            ans += sharks[(r, col)][0]
            del sharks[(r, col)]
            return


R, C, M = map(int, input().split())

sharks = {}
for i in range(M):
    shark_info = list(map(int, input().split()))
    if shark_info[3] < 3:
        shark_info[2] %= 2 * (R - 1)
    else:
        shark_info[2] %= 2 * (C - 1)
    sharks[(shark_info[0]-1, shark_info[1]-1)] = [shark_info[4], shark_info[3], shark_info[2]]
    # [크기, 방향, 속력]
ans = 0
for c in range(C):
    catch_shark(c)
    move_shark()
print(ans)
