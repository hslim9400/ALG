def subset(depth):
    global check, ans
    if depth == N:
        chosen = []
        for i in range(N):
            if check[i]:
                chosen.append(workers[i])
        if sum(chosen) >= B:
            if sum(chosen) < ans:
                ans = sum(chosen)
        return
    check[depth] = 0
    subset(depth+1)
    check[depth] = 1
    subset(depth+1)


T = int(input())
for test_case in range(1, T+1):
    N, B = map(int, input().split())
    workers = list(map(int, input().split()))
    ans = sum(workers)
    check = [0] * N
    subset(0)
    print(f'#{test_case} {ans-B}')
