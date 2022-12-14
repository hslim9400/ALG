def roll(current_facing, move):  # 주사위 굴리기
    # 방향에 따라 움직이는 면들을 밀어준다.
    if move == 0:
        current_facing['top'], current_facing['east'], current_facing['bottom'], current_facing['west'] = \
            current_facing['east'], current_facing['bottom'], current_facing['west'], current_facing['top']
    elif move == 1:
        current_facing['top'], current_facing['west'], current_facing['bottom'], current_facing['east'] = \
            current_facing['west'], current_facing['bottom'], current_facing['east'], current_facing['top']
    elif move == 2:
        current_facing['top'], current_facing['south'], current_facing['bottom'], current_facing['north'] = \
            current_facing['south'], current_facing['bottom'], current_facing['north'], current_facing['top']
    else:
        current_facing['top'], current_facing['south'], current_facing['bottom'], current_facing['north'] = \
            current_facing['north'], current_facing['top'], current_facing['south'], current_facing['bottom']
    return current_facing

# 자료구조
# dice : 한 면의 숫자를 키, 그 숫자에 적혀있는 값을 값으로 하는 딕셔너리
# current_facing : 위, 아래, 동서남북방향이 키, 그 방향을 어떤 면이 보고 있는지 값으로 하는 딕셔너리 
dice = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
current_facing = {'bottom': 6, 'top': 1, 'east': 3, 'west': 4, 'south': 5, 'north': 2}
N, M, x, y, k = map(int, input().split())
current = (x, y)
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]
moves = list(map(int, input().split()))

for move in moves:
    move -= 1
    if 0 <= current[0] + dr[move] < N and 0 <= current[1] + dc[move] < M:
        result = roll(current_facing, move)
        current_facing = result
        current = (current[0] + dr[move], current[1] + dc[move])
        r, c = current
        if board[r][c]:
            dice[current_facing['bottom']] = board[r][c]
            board[r][c] = 0
        else:
            board[r][c] = dice[current_facing['bottom']]
        print(dice[current_facing['top']])



