
def find_p(x):
    if not p[x] == x:
        p[x] = find_p(p[x])
    return p[x]


def union(x, y):
    p[find_p(x)] = find_p(y)


N = int(input())

cities = list(map(int, input().split()))
adj = [[0]*(N+1) for _ in range(N+1)]
for i in range(N):
    line = list(map(int, input().split()))
    for j in range(1, len(line)):
        adj[i+1][line[j]] = 1
        adj[line[j]][i+1] = 1

min_diff = 100 * N
for i in range(1<<N):
    group_a = set()
    group_b = set()
    p = list(range(N + 1))
    r = [0] * (N + 1)
    for j in range(N):
        if i & (1<<j):
            group_a.add(j)
        else:
            group_b.add(j)
    roots = set()
    for x in group_a:
        for y in group_a:
            if adj[x][y]:
                union(x, y)
    for x in group_b:
        for y in group_b:
            if adj[x][y]:
                union(x, y)
    for j in range(N):
        roots.add(find_p(j))
    a_population = 0
    b_population = 0
    group_a = list(group_a)
    group_b = list(group_b)
    if len(roots) != 2:
        continue
    print(roots, group_a, group_b)
    for k in range(len(group_a)):
        a_population += cities[group_a[k]]
    for k in range(len(group_b)):
        b_population += cities[group_b[k]]
    diff = abs(a_population - b_population)
    if diff < min_diff:
        min_diff = diff

print(min_diff)