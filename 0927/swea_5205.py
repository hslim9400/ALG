T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    print(f'#{test_case} {A[N//2]}')