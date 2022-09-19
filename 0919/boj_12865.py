
N, K = map(int, input().split())
things = []
memo = [[0]*(K+1) for _ in range(N+1)] # 이전 열로부터 누적합하므로 i+1, K의 무게를 사용할 것이므로 K+1
for _ in range(N):
    w, v = map(int, input().split())
    things.append((w, v))

for i in range(1, N+1):
    # 물건을 하나 꺼내서 무게가 K가 될 때 까지 1번부터 해당 물건을 조합하여 만들 수 있는 최대 가치를 찾는다.
    # 따라서 memo[i][j]는 1번부터 i번째 물건까지로 만들 수 있는 무게 j중 가장 높은 가치를 가진 조합이 될 것
    thing = things[i-1]
    for j in range(1, K+1):
        if j < thing[0]:  # 현재 물건보다 가벼운 무게라면 현재보다 앞의 물건까지만 반영
            memo[i][j] = memo[i-1][j]
        else:  # 현재 물건보다 무거워 지면 윗열에서 만든 가치와 비교한다.
            # 현재 열의 값을 사용하면 같은 물건을 두번 쓰는 꼴이 될 수 있다.
            if memo[i-1][j] < memo[i-1][j-thing[0]] + thing[1]:
                memo[i][j] = memo[i-1][j-thing[0]] + thing[1]
            else:
                memo[i][j] = memo[i-1][j]
print(memo[N][K])