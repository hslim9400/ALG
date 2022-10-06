from collections import deque

N, M, K =map(int, input().split())

board = [[5]*N for _ in range(N)]
trees = []
supply = []
stacks = [[0]*N for _ in range(N)]
for i in range(N):
    supply.append(list(map(int, input().split())))
for i in range(M):
    r, c, age = map(int, input().split())
    trees.append([r-1, c-1, age, 0])
trees.sort(key=lambda x: x[2])
year = 0
trees = deque(trees)

while year < K:
    die = []
    next_trees = deque()
    live = []
    for tree in trees:
        board[tree[0]][tree[1]] += (year - stacks[tree[0]][tree[1]]) * supply[tree[0]][tree[1]]
        stacks[tree[0]][tree[1]] = year
        if tree[2] > board[tree[0]][tree[1]]:
            die.append(tree)
        else:
            board[tree[0]][tree[1]] -= tree[2]
            tree[2] += 1
            live.append(tree)
            next_trees.append(tree)
    for tree in die:
        board[tree[0]][tree[1]] += tree[2]//2

    for tree in live:
        if not tree[2]%5:
            for dr in [0, 1, -1]:
                for dc in [0, 1, -1]:
                    if not dr and not dc:
                        continue
                    if 0 <= tree[0]+dr < N and 0 <= tree[1]+dc < N:
                        for new_tree in next_trees:
                            if new_tree[0] == tree[0]+dr and new_tree[1] == tree[1]+dc:
                                new_tree[3] += 1
                                continue
                        next_trees.appendleft([tree[0]+dr, tree[1]+dc, 1, 0])
    trees = next_trees

    year += 1

print(len(trees))
