from collections import deque


def simulate(current, end, next_d):
    global snake, body
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    d = snake['facing']
    while current < end:
        head = snake['snake'][-1]
        next_head = (head[0]+dr[d], head[1]+dc[d])
        if next_head in body:
            return current, True
        if 0 <= next_head[0] < N and 0 <= next_head[1] < N:
            snake['snake'].append(next_head)
            body.add(next_head)
        else:
            return current, True
        if board[next_head[0]][next_head[1]]:
            board[next_head[0]][next_head[1]] = 0
        else:
            tail = snake['snake'].popleft()
            body.discard(tail)
        current += 1
    snake['facing'] += next_d
    snake['facing'] %= 4

    return current, False


N = int(input())
K = int(input())
board = [[0]*N for _ in range(N)]
apples = []
for _ in range(K):
    r, c = map(int, input().split())
    board[r-1][c-1] = 1

L = int(input())
change_d = {'L': -1, 'D': 1}
moves = []
for _ in range(L):
    move = input().split()
    moves.append((int(move[0]), change_d[move[1]]))

current, finished = 1, False
snake = {'snake': deque([(0, 0)]), 'facing': 0}
body = set()
body.add((0, 0))
for move in moves:
    current, finished = simulate(current, move[0]+1, move[1])
    if move == moves[-1]:
        current, finished = simulate(current, 10000, 0)

    if finished:
        break
print(current)