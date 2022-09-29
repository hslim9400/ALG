def find_set(x):
    if p[x] != x:
        p[x] = find_set(p[x])
    return p[x]


def union(x, y):
    p[find_set(y)] = find_set(x)


T = int(input())

for test_case in range(1, T+1):
    V, E = map(int, input().split())
    p = list(range(V+1))

    edges = list(map(int, input().split()))

    for i in range(E):
        y, x = edges[2*i], edges[2*i + 1]
        if find_set(x) != find_set(y):
            union(x, y)
    roots = set()
    for i in range(1, V+1):
        roots.add(find_set(i))
    print(f'#{test_case} {len(roots)}')
