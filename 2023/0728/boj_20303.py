N, M, K = map(int, input().split())

children = list(map(int, input().split()))
adj = [[] for _ in range(N)]

for _ in range(M):
    start, end = map(int, input().split)