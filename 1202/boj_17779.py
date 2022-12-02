# 사용한 자료구조
# population_board: 인구 수가 적힌 2차원 배열(문제에서 줌)
# current_board: 나눈 구역을 표시하는 2차원 배열(시행마다 초기화)
# population: 구역별 인구 수를 계산할 딕셔너리(구역: 인구수)

# 구역 나누기 함수
# 경계선을 먼저 5로 그리고 모든 칸을 순회하며 조건에 따라 구역을 적어넣는다.
# if_five라면 경계선 내부, False라면 경계선 외부이다.
def divide_area(x, y, d_1, d_2):
    global current_board
    for i in range(d_1+1):
        for j in range(d_2+1):
            current_board[x+i][y-i] = 5
            current_board[x+j][y+j] = 5
            current_board[x+d_1+j][y-d_1+j] = 5
            current_board[x+d_2+i][y+d_2-i] = 5
    for r in range(N):
        if r == x or r == x + d_1 + d_2: # 5가 한개 나옴
            only_five = True
        else:
            only_five = False
        five = False
        for c in range(N):
            if current_board[r][c] == 5:  # 경계선
                if only_five:  # 5가 한 개만 나오니 종료
                    continue
                if five:
                    five = False  # 5가 끝남
                else:
                    five = True  # 5가 시작됨
            else:
                if five:  # 5가 진행중
                    current_board[r][c] = 5
                else:  # 5가 아닌 다른 구역 조건
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
for i in range(N):
    line = list(map(int, input().split()))
    population_board.append(line)
ans = 100 * N * N
for x in range(N):  # x, y, d_1, d_2경우를 완전탐색
    for y in range(1, N):
        for d_1 in range(1, y+1):
            for d_2 in range(1, N-y+1):
                if x+d_1+d_2 < N and 0 <= y-d_1 and y+d_2 < N: # for문의 범위를 잘 조절하면 없어도 되나?
                    current_board = [[0]*N for _ in range(N)]
                    divide_area(x, y, d_1, d_2)
                    population = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
                    for r in range(N):  # 나뉘어진 구역에 따라 인구수를 더함
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