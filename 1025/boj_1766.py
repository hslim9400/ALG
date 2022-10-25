import heapq

N, M = map(int, input().split())
nexts = {}
for i in range(1, N+1):
    nexts[i] = []
visited = [0] * (N+1)
ready = set(range(1, N+1))
pre_left = [0] * (N+1)

for _ in range(M):
    pre, post = map(int, input().split())
    nexts[pre].append(post)
    pre_left[post] += 1
    ready.discard(post)
ready = list(ready)
heapq.heapify(ready)
problems = N
ans = []
while problems:
    target = heapq.heappop(ready)
    ans.append(target)
    for post in nexts[target]:
        pre_left[post] -= 1
        if not pre_left[post]:
            heapq.heappush(ready, post)
    problems -= 1

print(*ans)
