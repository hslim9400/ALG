N = int(input())
orders = list(input())
current = (0, 0)
floors = {(0, 0)}
dr = [1, 0, -1, 0]
dc = [0, -1, 0, 1]
d = 0
max_r, max_c, min_r, min_c = 0, 0, 0, 0
for order in orders:
    r = current[0]
    c = current[1]
    if order == 'R':
        d += 1
        d %= 4
    elif order == 'L':
        d -= 1
        d %= 4
    else:
        r += dr[d]
        c += dc[d]
        current = (r, c)
        floors.add(current)
        if r > max_r:
            max_r = r
        if r < min_r:
            min_r = r
        if c > max_c:
            max_c = c
        if c < min_c:
            min_c = c
height = max_r - min_r + 1
width = max_c - min_c + 1

board = [['#']*width for _ in range(height)]
for floor in floors:
    r = floor[0] - min_r
    c = floor[1] - min_c
    board[r][c] = '.'
for i in range(height):
    print(''.join(board[i]))