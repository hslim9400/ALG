import heapq

T = int(input())
for test_case in range(1, T + 1):
    H, W, N = map(int, input().split())
    targets = list(map(len, (input().split())))
    current_max = max(targets)
    ans = 0

    while True:
        ans += 1
        current_w = 0
        current_h = ans

        for target in targets:
            if current_w:
                if current_w + ans * (target + 1) > W:
                    current_w = ans*target
                    current_h += ans
                    if current_w > W:
                        break
                else:
                    current_w += ans * (target + 1)
            else:
                current_w = ans*target
                if current_w > W:
                    break
            if current_h > H:
                break
        else:
            continue
        break

    print(f'#{test_case} {ans-1}')
