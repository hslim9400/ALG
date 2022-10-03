from collections import deque, defaultdict

def solution(n, paths, gates, summits):
    adj = defaultdict(list)
    INF = 100000000001
    for path in paths:
        adj[path[0]].append([path[1], path[2]])
        adj[path[1]].append([path[0], path[2]])

    summits = set(summits)
    intensities = [INF] * (n+1)
    queue = deque()
    for gate in gates:
        intensities[gate] = 0
        queue.append(gate)
    while queue:
        current = queue.popleft()
        if current in summits:
            continue
        for path in adj[current]:
            if intensities[path[0]] > max(intensities[current], path[1]):
                intensities[path[0]] = max(intensities[current], path[1])
                queue.append(path[0])
    ans = 0
    min_intensity = INF
    for summit in summits:
        if min_intensity > intensities[summit]:
            min_intensity = intensities[summit]
            ans = summit
        if min_intensity == intensities[summit]:
            if summit < ans:
                ans = summit

    answer = [ans, min_intensity]
    return answer

print(solution(6, [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]], [1,3], [5]))