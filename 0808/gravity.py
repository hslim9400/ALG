
T = int(input())

for test_case in range(1, T+1):

    N, M = list(map(int, input().split()))
    height_list = list(map(int, input().split()))
    max_fall = 0

    for i in range(N-1):
        fall_height = 0
        for j in range(i+1, N):
            if height_list[i] > height_list[j]:
                fall_height = fall_height + 1
        if fall_height > max_fall:
            max_fall = fall_height

    print(f'#{test_case} {max_fall}')



