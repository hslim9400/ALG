def find_set(x):
    if p[x] != x:
        p[x] = find_set(p[x])
    return p[x]


def union(x, y):
    p[find_set(y)] = find_set(x)


T = int(input())
for test_case in range(1, T+1):
    V, E = map(int, input().split())
    edges = []
    for i in range(E):
        start, end, cost = map(int, input().split())
        edges.append([cost, start, end])
    edges.sort()
    p = list(range(V+1))
    ans = 0
    counts = 0
    for i in range(E):
        cost, y, x = edges[i]
        if find_set(x) != find_set(y):
            union(x, y)
            ans += cost
            counts += 1
        if counts == V:
            break
    print(f'#{test_case} {ans}')
