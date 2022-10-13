
N = int(input())
board = [[0]*N for _ in range(N)]
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
students = {}
for _ in range(N*N):
    student_info = list(map(int, input().split()))
    student = student_info[0]
    prefer = set(student_info[1:])
    students[student] = prefer
    seat = (-1, -1)
    max_counts = 0
    max_empty = 0
    for r in range(N):
        for c in range(N):
            if board[r][c]:
                continue
            if seat == (-1, -1):
                seat = (r, c)
            counts = 0
            empty = 0
            for d in range(4):
                if 0 <= r+dr[d] < N and 0 <= c+dc[d] < N:
                    if board[r+dr[d]][c+dc[d]] in prefer:
                        counts += 1
                    if not board[r+dr[d]][c+dc[d]]:
                        empty += 1
            if counts > max_counts:
                max_counts = counts
                seat = (r, c)
                max_empty = empty
            elif counts == max_counts:
                if empty > max_empty:
                    max_empty = empty
                    seat = (r, c)

    board[seat[0]][seat[1]] = student

points = 0
for r in range(N):
    for c in range(N):
        student = board[r][c]
        counts = 0
        for d in range(4):
            if 0 <= r + dr[d] < N and 0 <= c + dc[d] < N:
                if board[r + dr[d]][c + dc[d]] in students[student]:
                    counts += 1
        if counts:
            points += 10**(counts-1)
print(points)