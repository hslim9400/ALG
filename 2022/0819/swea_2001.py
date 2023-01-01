T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    field = []
    max_fly = 0
    for j in range(N):
        field.append(list(map(int, input().split())))

    for i in range(N - M + 1):  # M칸을 확인 할 것이므로
        for j in range(N - M + 1):
            f = 0
            for k in range(M):  # M x M칸 내의 모든 파리를 더해준다.
                for l in range(M):
                    f = f + field[i + k][j + l]
            if f > max_fly:  # 최댓값 갱신
                max_fly = f

    print(f'#{test_case} {max_fly}')