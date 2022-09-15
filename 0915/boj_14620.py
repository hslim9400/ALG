N = int(input())
board = []
for i in range(N):
    board.append(list(map(int, input().split())))
min_price = N*N*200
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
for x1 in range(1, N-1):
    for y1 in range(1, N-1):
        for x2 in range(1, N-1):
            for y2 in range(1, N-1):
                if (x1, y1) == (x2, y2):
                    break
                for x3 in range(1, N-1):
                    for y3 in range(1, N-1):
                        if (x2, y2) == (x3, y3) or (x1, y1) == (x3, y3):
                            break
                        targets = {(x1,y1), (x2,y2), (x3,y3)}
                        for d in range(4):
                            targets.add((x1 + dx[d], y1 + dy[d]))
                            targets.add((x2 + dx[d], y2 + dy[d]))
                            targets.add((x3 + dx[d], y3 + dy[d]))
                        if len(targets) != 15:
                            break
                        price = 0
                        for target in targets:
                            price += board[target[0]][target[1]]
                            if price > min_price:
                                break
                        if price < min_price:
                            min_price = price
print(min_price)
