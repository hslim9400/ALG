def pour(x, y):
    y_space = y[1] - y[0]
    if x[0] <= y_space:
        return [0, x[1]], [y[0]+x[0], y[1]]
    else:
        return [x[0]-y_space, x[1]], [y[1], y[1]]


A, B, C = map(int, input().split())

queue = [(0, 0, C)]
visited = set()
while queue:
    current = queue.pop(0)
    if current in visited:
        continue
    visited.add(current)
    a = [current[0], A]
    b = [current[1], B]
    c = [current[2], C]
    next_steps = []
    for x in [a, b, c]:
        print(id(x), id(a))
        for y in [a, b, c]:
            if x != y and x[0]:
                x, y = pour(x, y)
                print(x, y, a, b, c)
                next_steps.append((a[0], b[0], c[0]))
    print(next_steps)
    for next_step in next_steps:
        if next_step not in visited:
            queue.append(next_step)
ans = []
for comb in visited:
    if not comb[0]:
        ans.append(comb[2])
ans.sort()
print(*ans)