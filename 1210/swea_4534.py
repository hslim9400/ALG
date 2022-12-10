from collections import deque
# CNS의 멀티탭 문제와 유사한 접근(DP)
# 트리구조를 만든 후 리프에서 루트까지 경우의 수를 쌓아 올라가며 해결
# 새로운 자식노드의 경우의 수를 반영할 때
# 부모의 색이 흰색이면
# 기록된 부모의 경우의 수 *= 새로운 자식의 흰 경우 + 검은 경우
# 부모가 검은색이면
# 기록된 부모의 경우의 수 *= 새로운 자식의 흰 경우

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    adj = [[] for _ in range(N+1)]
    for i in range(N-1):
        start, end = map(int, input().split())
        adj[start].append(end)
        adj[end].append(start)
    stack = [1]
    parent = [0] * (N+1)
    children = [set() for _ in range(N+1)]
    visited = set()
    while stack:
        current = stack.pop()
        if current in visited:
            continue
        visited.add(current)
        for destination in adj[current]:
            if destination not in visited:
                stack.append(destination)
                children[current].add(destination)
                parent[destination] = current

    result = [[0, 0] for _ in range(N+1)]
    # [흰 경우, 검은 경우, 완료 여부]

    queue = deque([])
    for i in range(1, N+1):
        if not children[i]:
            result[i][0], result[i][1] = 1, 1
            queue.append(i)

    while queue:
        current = queue.popleft()
        if children[current]:
            continue
        target = parent[current]
        if result[target] != [0, 0]:
            result[target][0] *= (result[current][0] + result[current][1])
            result[target][1] *= result[current][0]
        else:
            result[target][0] = result[current][0] + result[current][1]
            result[target][1] = result[current][0]
        children[target].discard(current)
        if not children[target] and target != 1:
            queue.append(target)

    ans = (result[1][0] + result[1][1]) % 1000000007
    print(f'#{test_case} {ans}')


