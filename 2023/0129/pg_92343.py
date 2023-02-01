def solution(info, edges):
    answer = 0

    adj = [[] for _ in range(len(info))]

    for edge in edges:
        adj[edge[0]].append(edge[1])
        adj[edge[1]].append(edge[0])

    visited = {0}

    def explore(node, sheeps, wolves, candidates):
        nonlocal answer, visited
        answer = max(answer, sheeps)
        print(node, sheeps, wolves, candidates)

        new_candidates = set(candidates)
        for adj_node in adj[node]:
            if adj_node not in visited:
                new_candidates.add(adj_node)
        for destination in new_candidates:
            if destination not in visited:
                visited.add(destination)
                if info[destination]:
                    if sheeps > wolves + 1:
                        explore(destination, sheeps, wolves+1, new_candidates)
                else:
                    explore(destination, sheeps+1, wolves, new_candidates)
                visited.discard(destination)

    explore(0, 1, 0, set(adj[0]))
    return answer

print(solution([0,1,0,1,1,0,1,0,0,1,0], [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]	))