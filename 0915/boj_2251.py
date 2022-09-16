def pour(x, y):  # 물을 옮기는 함수
    # x는 물을 줄 물통, y는 물을 받을 물통
    y_space = y[1] - y[0]  # 받을 물통의 남은 부피
    if x[0] <= y_space:  # 넘치지 않는 경우
        diff = x[0]  # 함수 끝나고 초기화를 위해 물을 얼마나 옮겼는지 남겨둠
        y[0] = y[0] + x[0]
        x[0] = 0
        return x, y, diff
    else:  # 넘치므로 멈춰야 하는 경우
        diff = y[1] - y[0]
        x[0] = x[0] - y_space
        y[0] = y[1]
        return x, y, diff


A, B, C = map(int, input().split())
# 물을 옮기며 나타날 수 있는 모든 경우의 수를 bfs로 찾을 예정
# 초기 값은 A통 0, B통 0, C통 C임
queue = [(0, 0, C)]
visited = set()
while queue:
    current = queue.pop(0)
    if current in visited:
        continue
    visited.add(current)
    a = [current[0], A]  # 물통의 현재 물 양, 최대 부피
    b = [current[1], B]
    c = [current[2], C]
    next_steps = []
    for x in [a, b, c]:
        for y in [a, b, c]:  # 물통 중 두개를 고르는 경우를 모두 탐색
            if x != y and x[0]:  # 물을 줄 물통이 비어있지 않다면
                x, y, diff = pour(x, y)  # 물을 옮긴다
                if 0 <= a[0] <= A and 0 <= b[0] <= B and 0 <= c[0] <= C:
                    next_steps.append((a[0], b[0], c[0]))
                x[0] += diff  # 다음 for문을 위해 물통 초기화
                y[0] -= diff
    for next_step in next_steps:
        if next_step not in visited:
            queue.append(next_step)
ans = []
for comb in visited:  # 문제 조건
    if not comb[0]:  # a물통에 물이 없을 때
        ans.append(comb[2])  # c 물통의 물 양
ans.sort()
print(*ans)