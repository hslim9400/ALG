T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    containers = list(map(int, input().split()))
    trucks = list(map(int, input().split()))
    containers.sort(reverse=True)
    trucks.sort(reverse=True)

    ans = 0
    for i in range(N):
        container = containers[i]
        for j in range(len(trucks)):
            if trucks:
                if trucks[0] >= container:
                    trucks.pop(0)
                    ans += container
                    break
    print(f'#{test_case} {ans}')
