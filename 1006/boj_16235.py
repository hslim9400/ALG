
N, M, K = map(int, input().split())

board = [[5]*N for _ in range(N)]
trees = [[[] for _ in range(N)] for _ in range(N)]
supply = []
stacks = [[0]*N for _ in range(N)]
for i in range(N):
    supply.append(list(map(int, input().split())))
for i in range(M):
    r, c, age = map(int, input().split())
    r, c = r-1, c-1
    trees[r][c].append(age)
for i in range(N):
    for j in range(N):
        trees[i][j].sort(reverse=True)
year = 0
while year < K:

    for r in range(N):
        for c in range(N):
            for idx in range(len(trees[r][c])-1, -1, -1):
                tree = trees[r][c]
                if tree[idx] > board[r][c]:
                    for dead in tree[:idx+1]:
                        board[r][c] += dead // 2
                    trees[r][c] = tree[idx+1:]
                    break
                board[r][c] -= tree[idx]
                tree[idx] += 1

    for r in range(N):
        for c in range(N):
            for tree in trees[r][c]:
                if not tree%5:
                    for dr in [0,1,-1]:
                        for dc in [0,1,-1]:
                            if (dr or dc) and 0<=r+dr<N and 0<=c+dc<N:
                                trees[r+dr][c+dc].append(1)

    for r in range(N):
        for c in range(N):
            board[r][c] += supply[r][c]

    year += 1
ans = 0
for r in range(N):
    for c in range(N):
        ans += len(trees[r][c])
print(ans)
