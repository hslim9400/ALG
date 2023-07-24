N, M, T = map(int, input().split())

board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

commands = []
for _ in range(T):
    commands.append(list(map(int, input().split())))