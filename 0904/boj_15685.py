def dragon_curve(x_current, y_current, current):
    global points, current_points
    if current == g+1:
        for point in current_points:
            points.append(point)
        return

    for i in range(len(current_points)-2, -1, -1):
        x_diff = x_current - current_points[i][0]
        y_diff = y_current - current_points[i][1]
        new_x = x_current + y_diff
        new_y = y_current - x_diff
        current_points.append((new_x, new_y))

    dragon_curve(new_x, new_y, current+1)


N = int(input())
points = []
dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]
for _ in range(N):
    x, y, d, g = map(int, input().split())
    current_points = []
    current_points.append((x, y))
    current_points.append((x+dx[d], y+dy[d]))
    dragon_curve(x+dx[d], y+dy[d], 1)

points = set(points)
ans = 0
for point in points:
    if (point[0]+1, point[1]) in points and  (point[0], point[1]+1) in points and (point[0]+1, point[1]+1) in points:
        ans += 1

print(ans)



