N, M = map(int, input().split())

board = []
for _ in range(N):
    board.append(list(input()))

direction = {
    'U': (-1, 0),
    'D': (1, 0),
    'R': (0, 1),
    'L': (0, -1)
}
visited = [[0]*M for _ in range(N)]
destination = set()
answer = 0

def search(r, c):
    global answer, destination
    while not visited[r][c]:
        visited[r][c] = 1
        nr = r + direction[board[r][c]][0]
        nc = c + direction[board[r][c]][1]
        r, c = nr, nc

    if (r, c) not in destination:
        destination.add((r, c))
        answer += 1
    

for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            print(i, j)
            search(i, j)
            print(destination)
print(answer)
