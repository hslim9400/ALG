def dfs(num):
    global visited
    visited.append(num)
    for i in nodes[num]:
        dfs(i)


V = int(input())
edges = list(map(int, input().split()))
nodes = [[] for _ in range(V+1)]
for i in range(V-1):
    start = edges[2*i]
    end = edges[2*i+1]
    nodes[start].append(end)
visited = []
dfs(1)
print(visited)
