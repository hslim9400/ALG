def solution(info, edges):
    answer = 0

    adj = [[] for _ in range(len(info))]  # 트리이지만 그냥 그래프로 생각하고 인접배열을 만든다.

    for edge in edges:
        adj[edge[0]].append(edge[1])
        adj[edge[1]].append(edge[0])

    visited = {0}

    def explore(node, sheeps, wolves, candidates):
        # 현재 노드, 현재 데리고 있는 양, 늑대의 수, 현재 visited들에서 갈 수 있는 노드들
        
        # 로직:
        # 새로운 노드를 방문할 때 마다 현재 노드와 인접한 노드들을 다음 행선지에 포함시킴
        # 만약 새로운 노드에 양이 있다면 늑대때문에 갈 수 없었던 노드가 갈 수 있는 곳으로
        # 바뀔지도..?
        nonlocal answer, visited
        answer = max(answer, sheeps)
        # 가장 많은 양을 답으로 만들기

        new_candidates = set(candidates)
        for adj_node in adj[node]:
            if adj_node not in visited:
                new_candidates.add(adj_node)
        for destination in new_candidates:
            if destination not in visited:
                visited.add(destination)
                if info[destination]:
                    if sheeps > wolves + 1:
                        # 다음 노드에 늑대가 있어도 양이 많기 때문에 가보기로 한다.
                        explore(destination, sheeps, wolves+1, new_candidates)
                else:
                    explore(destination, sheeps+1, wolves, new_candidates)
                visited.discard(destination)

    explore(0, 1, 0, set(adj[0]))
    return answer

print(solution([0,1,0,1,1,0,1,0,0,1,0], [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]	))