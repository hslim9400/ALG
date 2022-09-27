T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    B = list(map(int, input().split()))

    counts = 0
    for i in range(M):
        target = B[i]
        l = 0
        r = N - 1
        flag1 = False
        flag2 = False
        while l <= r:
            m = (l+r)//2
            if A[m] == target:
                counts += 1
                break
            if A[m] < target:
                if flag1:
                    break
                l = m + 1
                flag1 = True
                flag2 = False
            if A[m] > target:
                if flag2:
                    break
                r = m - 1
                flag2 = True
                flag1 = False

    print(f'#{test_case} {counts}')

