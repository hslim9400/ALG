N, M = map(int, input().split())
r, c, d = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
current = (r, c)
cleaned = set()
while True:

    cleaned.add(current)
    for i in range(4):
        new_d = (d - 1 - i) % 4
        if board[current[0] + dr[new_d]][current[1] + dc[new_d]] == 0 and\
                (current[0] + dr[new_d], current[1] + dc[new_d]) not in cleaned:
            current = (current[0] + dr[new_d], current[1] + dc[new_d])
            d = new_d
            break
    else:
        if board[current[0]-dr[d]][current[1]-dc[d]]:
            break
        current = (current[0]-dr[d], current[1]-dc[d])
print(len(cleaned))