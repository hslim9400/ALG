T = int(input()) # 문제였나

for test_case in range(1, T+1):
    N, M = map(int, input().split())

    for _ in range(M):
        depart, arrive = map(int, input().split())
    print(N-1)
