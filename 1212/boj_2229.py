
N = int(input())
scores = list(map(int, input().split()))
points = [0] * len(scores)
points[0] = 0
if len(scores) > 1:
    points[1] = abs(scores[1] - scores[0])

if len(scores) > 2:
    current = scores[:3]
    current_diff = max(current) - min(current)
    points[2] = current_diff

    for i in range(3, len(scores)):
        new = scores[i]
        prev = scores[i-1]
        current.append(new)
        if points[i-2] + abs(new - prev) > points[i-1] + (max(current) - min(current) - current_diff):
            points[i] = points[i-2] + abs(new - prev)
            current = [prev, new]
            current_diff = abs(new - prev)
        else:
            points[i] = points[i-1]
            if max(current) - min(current) > current_diff:
                points[i] = points[i-1] + max(current) - min(current) - current_diff
                current_diff = max(current) - min(current)

print(points[-1])
