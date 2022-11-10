from copy import deepcopy
dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, -1, -1, -1, 0, 1, 1, 1]
# 사용한 자료구조:
# fishes : 물고기 번호를 키, 좌표와 방향을 값으로 갖는 딕셔너리
# shark : 상어의 좌표와 방향이 저장된 리스트
# board : 물고기 번호, 좌표가 저장된 2차원 리스트


# 물고기를 움직이는 함수
def move_fishes(fishes, board, shark):

    for fish in range(1, 17):
        if fish in fishes.keys():
            r, c = fishes[fish][0]
            d = fishes[fish][1]
            for _ in range(8):
                nr, nc = r+dr[d], c+dc[d]
                if 0 <= nr < 4 and 0 <= nc < 4 and shark[0] != (nr, nc):
                    if board[nr][nc]:
                        target = board[nr][nc][0]
                        board[r][c], board[nr][nc] = board[nr][nc], board[r][c]
                        board[nr][nc][1] = d
                        fishes[fish][0], fishes[target][0] = fishes[target][0], fishes[fish][0]
                        fishes[fish][1] = d
                        break
                    else:
                        board[nr][nc] = board[r][c]
                        board[nr][nc][1] = d
                        board[r][c] = 0
                        fishes[fish] = [(nr, nc), d]
                        break
                else:
                    d += 1
                    d %= 8
    return fishes, board


# 상어를 움직이는 함수
# 상어가 갈 곳이 없다면 여기서 답을 냄
def move_shark(fishes, board, shark, point):
    global ans
    flag = True
    current = shark[0]
    d = shark[1]
    while True:
        r, c = current
        nr, nc = r+dr[d], c+dc[d]
        if 0 <= nr < 4 and 0 <= nc < 4:
            if board[nr][nc]:
                fish = board[nr][nc]
                new_point = point
                new_point += fish[0]
                new_shark = [(nr, nc), fish[1]]
                new_board = deepcopy(board)
                new_board[nr][nc] = 0
                new_fishes = deepcopy(fishes)
                del new_fishes[fish[0]]
                simulate(new_fishes, new_board, new_shark, new_point)
                flag = False # 움직일 수 있다면 답을 갱신하지 않음
            current = (nr, nc)
        else:
            break
    if flag:
        ans = max(ans, point)


# 위의 두 함수를 실행시키는 함수
# simulate에서 move_fish와 move_shark를 실행하고
# move_shark에서 다음 simulate를 실행하는 재귀 구조
def simulate(fishes, board, shark, point):
    new_fishes = deepcopy(fishes)
    new_board = deepcopy(board)
    next_fishes, next_board = move_fishes(new_fishes, new_board, shark)
    move_shark(next_fishes, next_board, shark, point)


fishes = {}
board = []
for i in range(4):
    line = list(map(int, input().split()))
    board_line = []
    for j in range(4):
        fish = line[2*j]
        direction = line[2*j + 1] - 1
        fishes[fish] = [(i, j), direction]
        board_line.append([fish, direction])
    board.append(board_line)

# 초기 세팅: (0, 0)에 상어가 들어가고 그 자리에 있던 물고기의 방향을 가짐
# 해당 자리의 물고기를 삭제
shark = [(0, 0), board[0][0][1]]
ans = board[0][0][0]
del fishes[board[0][0][0]]
board[0][0] = 0
simulate(fishes, board, shark, ans)
print(ans)