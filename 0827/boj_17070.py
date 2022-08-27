def right(head):
    if head[1] + 1 < N and board[head[0]][head[1]+1] != 1:
        return (head[0], head[1]+1), (head[0], head[1])
    else:
        return None, None


def down(head):
    if head[0] + 1 < N and board[head[0]+1][head[1]] != 1:
        return (head[0]+1, head[1]), (head[0], head[1])
    else:
        return None, None


def cross(head):
    if head[1] + 1 < N and head[0] + 1 < N and board[head[0]][head[1]+1] != 1 and \
            board[head[0]+1][head[1]] != 1 and board[head[0]+1][head[1]+1] != 1:
        return (head[0]+1, head[1]+1), (head[0], head[1])
    else:
        return None, None


def move(head, tail):
    global answer
    if head == (N-1, N-1):
        answer += 1
        return

    if head[0] == tail[0]:
        new_head, new_tail = right(head)
        if new_head:
            move(new_head, new_tail)
        new_head, new_tail = cross(head)
        if new_head:
            move(new_head, new_tail)
    elif head[1] == tail[1]:
        new_head, new_tail = down(head)
        if new_head:
            move(new_head, new_tail)
        new_head, new_tail = cross(head)
        if new_head:
            move(new_head, new_tail)
    else:
        new_head, new_tail = right(head)
        if new_head:
            move(new_head, new_tail)
        new_head, new_tail = down(head)
        if new_head:
            move(new_head, new_tail)
        new_head, new_tail = cross(head)
        if new_head:
            move(new_head, new_tail)


N = int(input())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

flag = True
if board[N-1][N-1] == 1:
    print(0)
    flag = False
if flag:
    answer = 0
    move((0,1), (0,0))
    print(answer)


