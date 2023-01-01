def find(n):  # 점화식
    if n >= len(memo):  # 메모이제이션, 재귀
        memo.append(find(n-1) + 2 * find(n-2))
    return memo[n]


T = int(input())
for test_case in range(1, T+1):
    N = int(input()) // 10  # 길이가 10단위인데 1단위로 변경
    memo = [1, 1]  # 총 길이가 0, 1일때 가능한 방법들
    ans = find(N)  # 가로길이가 N일때 점화식으로 값을 찾아줌
    print(f'#{test_case} {ans}')
