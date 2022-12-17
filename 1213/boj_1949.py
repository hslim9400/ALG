from collections import deque
# 아이디어: 트리DP
# 퐁당퐁당보다 퐁당당퐁이 더 클 수 있다는 것을 기억
# 자식 마을이 우수마을일 경우, 자식마을이 우수마을이 아니고 내가 우수마을일 경우, 자식마을도 우수마을이 아니고 나도 우수마을이 아닌경우
# 세 가지 경우를 쌓아 올라간다. 주변에 우수마을이 하나도 없는 경우는 어차피 최댓값 선정에서 탈락하기 때문에
# 따로 고려하지 않음.

N = int(input())
populations = [0] + list(map(int, input().split()))
adj = [[] for _ in range(N+1)]
for i in range(N-1):
    start, end = map(int, input().split())
    adj[start].append(end)
    adj[end].append(start)

parent = [0] * (N+1)
children = [set() for _ in range(N+1)]
stack = [1]
visited = set()
while stack:  # 1을 루트로 트리를 구성해줌
    current = stack.pop()
    if current in visited:
        continue
    visited.add(current)
    for destination in adj[current]:
        if destination not in visited:
            stack.append(destination)
            parent[destination] = current
            children[current].add(destination)

result = [[0, 0, 0] for _ in range(N+1)]
# 우수마을
queue = deque([])
for i in range(1, N+1):
    if not children[i]:
        queue.append(i)

while queue:
    current = queue.popleft()
    if children[current] or current == 1:
        continue
    result[current][0] += populations[current]
    target = parent[current]  # 부모에 경우를 더할 것임.
    result[target][0] += max(result[current][1], result[current][2])
    # 부모가 우수마을이면 자식은 반드시 우수마을이 아님.
    result[target][1] += result[current][0]
    # 부모가 우수마을이 아니고 자식은 우수마을인 경우
    result[target][2] += max(result[current][0], result[current][2])
    # 부모도 우수마을이 아니고 자식도 우수마을이 아닌 경우를 포함
    children[target].discard(current)
    if not children[target]:  # 자식이 없다면 이 녀석의 부모로 올릴 준비가 완료됨.
        queue.append(target)
result[1][0] += populations[1]
print(max(result[1]))
