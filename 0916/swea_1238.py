T = 10
for test_case in range(1, T+1):
    N, current_0 = map(int, input().split())
    adj = [[] for _ in range(101)]
    edges = list(map(int, input().split()))
    for i in range(N//2):
        start = edges[2*i]
        end = edges[2*i + 1]
        adj[start].append(end)

    queue = [(current_0, 0)]
    visited = set()
    contact = []
    while queue:
        current = queue.pop(0)
        place = current[0]
        dist = current[1]
        if place in visited:
            continue
        visited.add(place)
        contact.append(current)
        for destination in adj[place]:
            if destination not in visited:
                queue.append((destination, dist+1))

    contact.sort(key= lambda x: (x[1], x[0]))
    print(f'#{test_case} {contact[-1][0]}')
