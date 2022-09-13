def dfs(n):
    global ans
    if nodes[n]:
        dfs(nodes[n][0])
    ans += vals[n]
    if len(nodes[n]) == 2:
        dfs(nodes[n][1])


T = 10
for test_case in range(1, T+1):
    N = int(input())
    vals = ['' for _ in range(N+1)]
    nodes = [[] for _ in range(N+1)]

    for i in range(N):
        node = input().split()
        node_num = int(node[0])
        vals[node_num] = node[1]
        if len(node) >= 3:
            nodes[node_num].append(int(node[2]))
        if len(node) == 4:
            nodes[node_num].append(int(node[3]))
    ans = ''
    dfs(1)
    print(f'#{test_case} {ans}')
