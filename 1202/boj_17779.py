
def divide_area(x, y, d_1, d_2):
    global current_board
    for i in range(d_1+1):
        for j in range(d_2+1):
            current_board[x+i][y-i] = 5
            current_board[x+j][y+j] = 5
            current_board[x+d_1+j][y-d_1+j] = 5
            current_board[x+d_2+i][y+d_2-i] = 5
    for r in range(N):
        if r == x or r == x + d_1 + d_2:
            only_five = True
        else:
            only_five = False
        five = False
        for c in range(N):
            if current_board[r][c] == 5:
                if only_five:
                    continue
                if five:
                    five = False
                else:
                    five = True
            else:
                if five:
                    current_board[r][c] = 5
                else:
                    if r < x+d_1 and c <= y:
                        current_board[r][c] = 1
                    elif r <= x+d_2 and y <= c:
                        current_board[r][c] = 2
                    elif c < y-d_1+d_2:
                        current_board[r][c] = 3
                    else:
                        current_board[r][c] = 4


N = int(input())
population_board = []
election_board = [[0]*N for _ in range(N)]
for i in range(N):
    line = list(map(int, input().split()))
    population_board.append(line)
ans = 100 * N * N
for x in range(N):
    for y in range(1, N):
        for d_1 in range(1, y+1):
            for d_2 in range(1, N-y+1):
                if x+d_1+d_2 < N and 0 <= y-d_1 and y+d_2 < N:
                    current_board = [[0]*N for _ in range(N)]
                    divide_area(x, y, d_1, d_2)
                    population = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
                    for r in range(N):
                        for c in range(N):
                            population[current_board[r][c]] += population_board[r][c]
                    max_population = 0
                    min_population = 100 * N * N
                    for k in range(1, 6):
                        if max_population < population[k]:
                            max_population = population[k]
                        if min_population > population[k]:
                            min_population = population[k]
                    ans = min(ans, max_population-min_population)

print(ans)