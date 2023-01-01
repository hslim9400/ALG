T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    for i in range(1, 10**6+1):
        if i**3 == N:
            print(f'#{test_case} {i}')
            break
        if i**3 > N:
            print(f'#{test_case} {-1}')
            break
    else:
        print(f'#{test_case} {-1}')
