from collections import deque
def solution(n, path, order):
    answer = True
    left = n
    req_dict = {}
    next_dict = {}
    adj = [[] for _ in range(left)]
    for edge in path:
        start, end = edge
        adj[start].append(end)
        adj[end].append(start)
    visited = set()
    queue = deque([0])
    parents = {}
    while queue:  # 트리 만들기
        current = queue.popleft()
        if current in visited:
            continue
        visited.add(current)
        for destination in adj[current]:
            if destination not in visited:
                parents[destination] = current
                queue.append(destination)
                
    for req in order:
        prev, after = req
        req_dict[after] = prev
        next_dict[prev] = after
    queue = deque([0])
    visited = set()
    
    while queue:
        current = queue.popleft()
        if current in req_dict.keys():
            if req_dict[current] not in visited:
                continue
        if current in visited:
            continue
        visited.add(current)
        left -= 1
        for destination in adj[current]:
            if destination not in visited:
                queue.append(destination)
        if current in next_dict.keys():
            if parents[next_dict[current]] in visited:
                queue.append(next_dict[current])
        
    if left:
        answer = False
    return answer