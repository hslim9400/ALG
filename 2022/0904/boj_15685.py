def dragon_curve(x_current, y_current, current):
    global points, current_points
    if current == g+1:  # 모든 커브를 그렸다면
        for point in current_points:  # 점들을 다 추가해준다.
            points.append(point)
        return

    for i in range(len(current_points)-2, -1, -1):
        # 회전행렬이라는 녀석이 있다.
        # 어떤 좌표에
        # (cos, -sin)
        # (sin,  cos)의 2x2행렬을 곱해주면 원점을 기준으로 각도만큼 회전한 좌표가 계산된다.
        # 90도를 회전하면
        # (0, 1)
        # (-1, 0)를 곱해주면 원점을 기준으로 270도(시계방향으로 90도) 회전한 행렬이 나옴
        x_diff = x_current - current_points[i][0]  # 원점을 기준으로 해야하므로 상대좌표를 구해준다
        y_diff = y_current - current_points[i][1]
        new_x = x_current + y_diff  # 위의 행렬을 적용했다 치면 (x_current, y_current)를 기준으로 새로운 x는 y가 되고
        new_y = y_current - x_diff  # y는 -x가 된다.
        current_points.append((new_x, new_y))

    dragon_curve(new_x, new_y, current+1)


N = int(input())
points = []
dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]
for _ in range(N):
    x, y, d, g = map(int, input().split())  # 입력 명령
    current_points = []
    current_points.append((x, y))
    current_points.append((x+dx[d], y+dy[d]))
    dragon_curve(x+dx[d], y+dy[d], 1)

points = set(points)
ans = 0
for point in points:  # 사각형이 만들어질 때마다 카운트 +1
    if (point[0]+1, point[1]) in points and  (point[0], point[1]+1) in points and (point[0]+1, point[1]+1) in points:
        ans += 1

print(ans)



