def solution(edges, target):
    target = [0] + target
    answer = []
    children = [[] for _ in range(len(target))]
    nodes = set()
    # 리프가 도는 순서는 정해져있음
    # 일단 리프들에 3, 2, 1순서로 던지며 target을 맞추고
    # 숫자가 맞다면 2를 1, 1로, 3을 2, 1로 바꾸며 한 턴씩 벌어줌

    for edge in edges:
        parent = edge[0]
        child = edge[1]
        children[parent].append(child)
        nodes.add(parent)
        nodes.add(child)

    leaves = {}
    for node in nodes:
        if target[node]: 
            leaves[node] = {1: 0, 2: 0, 3: 0}
        else:  # 정렬하고 0을 추가하여 어떤 인덱스가 현재 선택된 길인지 표시
            children[node].sort()
            children[node].append(0)
    finished = set()
    cycle = []
    while True:
        leaf = 1
        while children[leaf]:
            child = children[leaf][children[leaf][-1]]  # 이번 길의 자식을 고르고
            children[leaf][-1] += 1  # 아까 추가한 0을 이용해 길을 변경해줌
            children[leaf][-1] %= len(children[leaf]) - 1
            leaf = child
        cycle.append(leaf)
        target_point = leaves[leaf][1] + 2*leaves[leaf][2] + 3*leaves[leaf][3]
        if target_point == target[leaf]:
            if leaves[leaf][2]:
                leaves[leaf][2] -= 1
                leaves[leaf][1] += 2
            elif leaves[leaf][3]:
                leaves[leaf][3] -= 1
                leaves[leaf][2] += 1
                leaves[leaf][1] += 1
            else:
                return [-1]
        else:
            if target_point == target[leaf] - 1:
                leaves[leaf][1] += 1
                target_point += 1
            elif target_point == target[leaf] - 2:
                leaves[leaf][2] += 1
                target_point += 2
            else:
                leaves[leaf][3] += 1
                target_point += 3
        if target_point == target[leaf]:
            finished.add(leaf)
            if len(finished) == len(leaves):
                break

    for leaf in leaves:
        leaves[leaf] = [3]*leaves[leaf][3] + [2]*leaves[leaf][2] + [1]*leaves[leaf][1]
    for node in cycle:
        num = leaves[node].pop()
        answer.append(num)

    return answer

