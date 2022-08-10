T = int(input())

for test_case in range(T):

    N = int(input())
    arr = []
    for _ in range(N):
        arr = arr + [(list(map(int, input().split())))]

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    total_sum = 0

    for i in range(N):
        for j in range(N):
            for k in range(4):
                x = i + dx[k]
                y = j + dy[k]
                if (0 <= x < N) and (0 <= y < N):
                    total_sum = total_sum + abs(arr[i][j]-arr[x][y])

    print(f'#{test_case} {total_sum}')

