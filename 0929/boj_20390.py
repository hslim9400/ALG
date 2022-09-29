import sys
sys.setrecursionlimit(100001)


def find_edge(node):
    global visited, dists, total_dists
    visited.add(node)
    if len(visited) == N:
        return

    cand = (1 << 81, N+1)
    for j in range(N):
        if j in visited:
            continue
        if node < j:
            dists[j] = min(dists[j], ((costs[node]*A + costs[j]*B) % C) ^ D)
        else:
            dists[j] = min(dists[j], ((costs[j] * A + costs[node] * B) % C) ^ D)
        if cand[0] > dists[j]:
            cand = (dists[j], j)
    total_dists += cand[0]
    find_edge(cand[1])


N = int(input())
A, B, C, D = map(int, input().split())
costs = list(map(int, input().split()))
large = 1 << 100
dists = [large] * N
visited = set()
total_dists = 0
find_edge(0)
print(total_dists)
