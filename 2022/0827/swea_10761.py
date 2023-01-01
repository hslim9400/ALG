T = int(input())

for test_case in range(1, T+1):
    N, *buttons = input().split()
    time = 0
    robots = {'B': [1, 0], 'O': [1, 0]}
    for i in range(int(N)):
        robot = buttons[2*i]
        target = int(buttons[2*i + 1])
        dist = abs(target - robots[robot][0])
        if time - robots[robot][1] >= dist:
            time += 1
        else:
            time += dist + 1 - (time - robots[robot][1])
        robots[robot][0] = target
        robots[robot][1] = time

    print(f'#{test_case} {time}')
