N, K = map(int, input().split())

jewels = []
bags = []
for _ in range(N):
    jewels.append(list(map(int, input().split)))

for _ in range(K):
    bags.append(int(input()))