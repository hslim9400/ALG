def solution(info, edges):
    answer = 0
    children = [[] for _ in range(len(info))]
    for i in range(len(info)):
        info[i] = [info[i], 0]

    for edge in edges:
        children[edge[0]].append(edge[1])

    def dfs(node, current_sheep, current_wolf):
        nonlocal finish, sheep, wolf, met_wolves
        for child in children[node]:
            if info[child][0]:
                if current_sheep == current_wolf + 1:
                    met_wolves = []
                    continue
                if not info[child][1]:
                    met_wolves.append(child)
                    dfs(child, current_sheep, current_wolf+1)
                    if met_wolves and met_wolves[-1] == child:
                        met_wolves.pop()
                else:
                    dfs(child, current_sheep, current_wolf)
            else:
                if not info[child][1]:
                    info[child][1] = 1
                    sheep += 1
                    for met_wolf in met_wolves:
                        info[met_wolf][1] = 1
                        wolf += 1
                    met_wolves = []
                    finish = False
                    dfs(child, sheep, wolf)
                else:
                    dfs(child, sheep, wolf)

    finish = False
    sheep = 1
    wolf = 0
    while not finish:
        finish = True
        met_wolves = []
        dfs(0, sheep, wolf)

    answer = sheep
    return answer

solution([0,1,0,1,1,0,1,0,0,1,0], [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]])