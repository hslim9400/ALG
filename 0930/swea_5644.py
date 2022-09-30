T = int(input())
for test_case in range(1, T+1):
    M, A = map(int, input().split())
    user = {'A': [1, 1], 'B': [10, 10]}
    dc = [0, -1, 0, 1, 0]
    dr = [0, 0, 1, 0, -1]

    moves_a = list(map(int, input().split()))
    moves_b = list(map(int, input().split()))

    chargers = {}
    for i in range(A):
        r, c, d, p = list(map(int, input().split()))
        chargers[(r, c)] = (d, p)

    t = 0
    total = 0
    while True:
        targets_a = []
        targets_b = []
        for charger in chargers.keys():
            if abs(user['A'][0] - charger[0]) + abs(user['A'][1] - charger[1]) <= chargers[charger][0]:
                targets_a.append((charger, chargers[charger][1]))
            if abs(user['B'][0] - charger[0]) + abs(user['B'][1] - charger[1]) <= chargers[charger][0]:
                targets_b.append((charger, chargers[charger][1]))
        targets_a.sort(key=lambda x: x[1], reverse=True)
        targets_b.sort(key=lambda x: x[1], reverse=True)
        if targets_a and targets_b:
            if targets_a[0] == targets_b[0]:
                if len(targets_a) > 1 and len(targets_b) > 1:
                    total += targets_a[0][1] + max(targets_a[1][1], targets_b[1][1])
                elif len(targets_a) > 1:
                    total += targets_b[0][1] + targets_a[1][1]
                elif len(targets_b) > 1:
                    total += targets_a[0][1] + targets_b[1][1]
                else:
                    total += targets_a[0][1]
            else:
                total += targets_a[0][1] + targets_b[0][1]
        else:
            if targets_a:
                total += targets_a[0][1]
            elif targets_b:
                total += targets_b[0][1]

        if t == M:
            break
        move_a = moves_a[t]
        move_b = moves_b[t]
        user['A'][0] += dr[move_a]
        user['A'][1] += dc[move_a]
        user['B'][0] += dr[move_b]
        user['B'][1] += dc[move_b]
        t += 1

    print(f'#{test_case} {total}')
