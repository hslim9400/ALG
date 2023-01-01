N = int(input())
orders = list(input())
current = (0, 0)  # 첫 위치를 (0,0)으로 할 것
floors = {(0, 0)}
dr = [1, 0, -1, 0]
dc = [0, -1, 0, 1]
d = 0
max_r, max_c, min_r, min_c = 0, 0, 0, 0  # 나중에 최솟값을 (0,0)으로 해서 미로를 그릴 예정
for order in orders:
    r = current[0]
    c = current[1]
    if order == 'R':  # 방향전환
        d += 1
        d %= 4
    elif order == 'L':
        d -= 1
        d %= 4
    else:
        r += dr[d]
        c += dc[d]
        current = (r, c)  # 움직인 후 위치를 잡고
        floors.add(current)  # 그 좌표 저장
        if r > max_r:  # 최댓값과 최솟값을 갱신
            max_r = r
        if r < min_r:
            min_r = r
        if c > max_c:
            max_c = c
        if c < min_c:
            min_c = c
height = max_r - min_r + 1  # 미로의 높이
width = max_c - min_c + 1  # 넓이

board = [['#']*width for _ in range(height)]  # 미로의 크기만큼 2차원 배열 생성
for floor in floors:
    r = floor[0] - min_r  # 최솟값이 (0,0)이 되도록 해서 미로를 완성해나간다.
    c = floor[1] - min_c
    board[r][c] = '.'
for i in range(height):
    print(''.join(board[i]))