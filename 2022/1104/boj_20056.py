def move(fireballs):  # 불덩이 옮기기
    directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
    new_balls = {}  # 옮긴 불덩이를 담아줌
    for location in fireballs.keys(): # 불덩이가 있는 좌표
        r, c = location
        for fireball in fireballs[location]:  # 좌표에 있는 불덩이
            m, s, d = fireball
            nr, nc = (r + s*directions[d][0]) % N, (c + s*directions[d][1]) % N
            if (nr, nc) in new_balls.keys():
                new_balls[(nr, nc)].append(fireball)
            else:
                new_balls[(nr, nc)] = [fireball]
    return new_balls


def after_move(fireballs):  # 옮겨진 불덩이 합치고 나누기
    for location in fireballs.keys():  # 불덩이가 있는 좌표
        counts = len(fireballs[location])  # 불덩이가 하나면 시행하지 않음
        if counts < 2:
            continue
        m = 0  # 질량을 더해줄 것
        v = 0  # 속력을 더해줄 것
        flag = True
        if fireballs[location][0][2] % 2:
            p = 1
        else:
            p = 0
        for fireball in fireballs[location]:
            m += fireball[0]
            v += fireball[1]
            if fireball[2] % 2:  # 홀, 짝을 모두 포함하면 flag가 False가 될 것
                if not p:
                    flag = False
            else:
                if p:
                    flag = False
        if m > 4:  # 5로 나눈 몫이 0이라면 없어질 것.
            if flag:
                fireballs[location] = [
                    [m // 5, v // counts, 0],
                    [m // 5, v // counts, 2],
                    [m // 5, v // counts, 4],
                    [m // 5, v // counts, 6]
                ]
            else:
                fireballs[location] = [
                    [m // 5, v // counts, 1],
                    [m // 5, v // counts, 3],
                    [m // 5, v // counts, 5],
                    [m // 5, v // counts, 7]
                ]
        else:
            fireballs[location] = []
    return fireballs


N, M, K = map(int, input().split())
fireballs = {}

for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    fireballs[(r, c)] = [[m, s, d]]

for _ in range(K):
    fireballs = move(fireballs)
    fireballs = after_move(fireballs)

ans = 0
for location in fireballs.keys():
    for fireball in fireballs[location]:
        ans += fireball[0]
print(ans)