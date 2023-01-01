def rotate(n, d):
    global wheels

    queue = [(n, d)]  # 현 톱니의 번호와 회전방향
    rotate_list = []
    while queue:
        current = queue.pop(0)  # 대기중인 톱니 회전
        if current in rotate_list:
            continue
        rotate_list.append(current)
        if current[0]-1 >= 0:  # 왼쪽에 톱니가 있다면
            if wheels[current[0]][6] != wheels[current[0]-1][2]:  # 회전 할 조건
                queue.append((current[0]-1, -current[1]))  # 회전 대기 목록에 추가
        if current[0]+1 < 4:  # 오른 쪽 마찬가지
            if wheels[current[0]][2] != wheels[current[0]+1][6]:
                queue.append((current[0]+1, -current[1]))
    for target in rotate_list:  # 톱니들 돌려주기
        if target[1] == 1:
            wheels[target[0]] = [wheels[target[0]][7]] + wheels[target[0]][:7]
        else:
            wheels[target[0]] = wheels[target[0]][1:] + [wheels[target[0]][0]]


wheels = []
for _ in range(4):
    wheel = list(map(int, list(input())))
    wheels.append(wheel)
K = int(input())
for _ in range(K):  # 입력에 맞게 톱니 회전
    n, d = map(int, input().split())
    rotate(n-1, d)
ans = 0
for i in range(4):  # 점수 계산 조건
    ans += wheels[i][0] * (2**i)
print(ans)
