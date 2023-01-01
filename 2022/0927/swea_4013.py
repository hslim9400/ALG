def rotate(target, order):
    global magnets

    targets = set()
    queue = [(target, order)]
    while queue:
        current, current_order = queue.pop(0)
        if (current, current_order) in targets:
            continue
        targets.add((current, current_order))
        for d in [1, -1]:
            if 0 <= current + d < 4:
                if magnets[current][2*d] + magnets[current+d][-2*d] == 1:
                    if (current+d, -current_order) not in targets:
                        queue.append((current+d, -current_order))
    targets = list(targets)
    for i in range(len(targets)):
        if targets[i][1] == 1:
            magnets[targets[i][0]] = ([magnets[targets[i][0]][-1]] + magnets[targets[i][0]])[:-1]
        else:
            magnets[targets[i][0]] = (magnets[targets[i][0]] + [magnets[targets[i][0]][0]])[1:]


T = int(input())
for test_case in range(1, T+1):
    K = int(input())
    magnets = []
    for i in range(4):
        magnets.append(list(map(int, input().split())))

    for k in range(K):
        target, order = map(int, input().split())
        rotate(target-1, order)
    ans = 0
    for i in range(4):
        ans += magnets[i][0] * (2**i)
    print(f'#{test_case} {ans}')

