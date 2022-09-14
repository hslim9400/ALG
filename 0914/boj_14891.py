def rotate(n, d):
    global wheels

    queue = [(n, d)]
    rotate_list = []
    while queue:
        current = queue.pop(0)
        if current in rotate_list:
            continue
        rotate_list.append(current)
        if current[0]-1 >= 0:
            if wheels[current[0]][6] != wheels[current[0]-1][2]:
                queue.append((current[0]-1, -current[1]))
        if current[0]+1 < 4:
            if wheels[current[0]][2] != wheels[current[0]+1][6]:
                queue.append((current[0]+1, -current[1]))
    for target in rotate_list:
        if target[1] == 1:
            wheels[target[0]] = [wheels[target[0]][7]] + wheels[target[0]][:7]
        else:
            wheels[target[0]] = wheels[target[0]][1:] + [wheels[target[0]][0]]


wheels = []
for _ in range(4):
    wheel = list(map(int, list(input())))
    wheels.append(wheel)
K = int(input())
for _ in range(K):
    n, d = map(int, input().split())
    rotate(n-1, d)
ans = 0
for i in range(4):
    ans += wheels[i][0] * (2**i)
print(ans)
