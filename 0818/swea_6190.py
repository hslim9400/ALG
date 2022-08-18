T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    num_list = list(map(int, input().split()))

    ans = -1
    for i in range(N):
        for j in range(i+1, N):
            target = str(num_list[i] * num_list[j])
            for k in range(len(target)-1):
                if target[k] > target[k+1]:
                    break
            else:
                if int(target) > ans:
                    ans = int(target)

    print(f'#{test_case} {ans}')