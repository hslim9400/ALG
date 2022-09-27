def quick_sort(target):
    n = len(target)
    if n <= 1:
        return target

    pivot = 0
    l = 0
    r = n - 1
    while True:
        for i in range(l, n):
            if target[i] > target[pivot]:
                l = i
                break
        else:
            l = n

        for i in range(r, pivot-1, -1):
            if target[i] < target[pivot]:
                r = i
                break
        else:
            r = 0
        if r <= l:
            target[pivot], target[r] = target[r], target[pivot]
            pivot = r
            break
        target[l], target[r] = target[r], target[l]


    return quick_sort(target[:pivot]) + [target[pivot]] + quick_sort(target[pivot+1:])


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))
    A = quick_sort(A)
    print(f'#{test_case} {A[N//2]}')
