T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    cheese = list(map(int, input().split()))
    for i in range(M):
        cheese[i] = [cheese[i], i+1]
    queue = []
    for i in range(N):
        queue.append(cheese.pop(0))

    while len(queue) > 1:
        current = queue.pop(0)
        current[0] = current[0]//2
        if current[0] == 0:
            if cheese:
                queue.append(cheese.pop(0))
            continue
        queue.append(current)

    print(f'#{test_case} {queue[0][1]}')
