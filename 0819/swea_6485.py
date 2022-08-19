T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    stops = [0] * 5000  # 정류장들
    for _ in range(N):
        A, B = map(int, input().split())
        for i in range(A-1, B):  # 정류장 번호는 1부터 시작하므로
            stops[i] += 1  # 해당 정류장을 지나는 노선의 개수 +1
    P = int(input())
    C = []
    for __ in range(P):
        C.append(int(input()))

    ans = []
    for i in range(len(C)):  # 답으로 P개의 정류장을 출력해야 한다
        ans.append(stops[C[i]-1])
    print(f'#{test_case}', *ans)
