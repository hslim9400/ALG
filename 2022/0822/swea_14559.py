T = int(input())
for test_case in range(1, T+1):
    N, S, E = map(int, input().split())
    M = int(input())
    A = []
    B = []
    for i in range(M):  # A와 B에 넣기
        Ai, Bi = map(int, input().split())
        A.append(Ai)
        B.append(Bi)


