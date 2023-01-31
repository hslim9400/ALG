from collections import deque
def solution(info, edges):
    answer = 0
    children = [[] for _ in range(len(info))]
    parents = [0 for _ in range(len(info))]

    for edge in edges:
        children[edge[0]].append(edge[1])

    def bfs():
        nonlocal finish, visited, wolves, sheeps
        queue = deque([[0, sheeps-wolves]])
        while queue:
            print(queue)
            print(visited)
            current = queue.popleft()
            current, left_sheep = current
            if current in visited:
                for child in children[current]:
                    queue.append([child, left_sheep])
                continue
            for child in children[current]:
                if info[child]:
                    if left_sheep > 2:
                        queue.append([child, left_sheep-1])
                else:
                    finish = False
                    node = child
                    sheeps += 1
                    visited.add(node)
                    node = parents[node]
                    while node not in visited:
                        wolves += 1
                        visited.add(node)
                        node = parents[node]
                    queue.append([child, left_sheep+1])

    finish = False
    sheeps = 1
    wolves = 0
    visited = set()
    while not finish:
        finish = True
        bfs()

    answer = sheeps
    return answer

print(solution([0,0,1,1,1,0,1,0,1,0,1,1], [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]))