def add_number(number, current):  # 모든 경우의 수를 완전탐색
    global num_list
    if len(number) == 6:
        if number not in num_list:
            num_list.append(number)
        return
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    for d in range(4):  # 네 방향 탐색
        if 0 <= current[0] + dr[d] < 5 and 0 <= current[1] + dc[d] < 5:
            new_number = number + board[current[0]+dr[d]][current[1]+dc[d]]
            add_number(new_number, (current[0]+dr[d], current[1]+dc[d]))



board = []
for _ in range(5):
    board.append(input().split())
num_list = []
for i in range(5):  # 모든 시적점에 대해 완전탐색
    for j in range(5):
        add_number('', (i,j))
print(len(num_list))