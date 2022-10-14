
N = int(input())
board = [[0]*N for _ in range(N)]
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
students = {}
for _ in range(N*N):  # 입력받는 학생 순으로 자리를 배정
    student_info = list(map(int, input().split()))
    student = student_info[0]  # 학생번호
    prefer = set(student_info[1:])  # 얘가 좋아하는 애들
    students[student] = prefer  # 나중을 위해 딕셔너리에 저장
    seat = (-1, -1)
    max_counts = 0
    max_empty = 0
    for r in range(N):
        for c in range(N):
            if board[r][c]:
                continue
            if seat == (-1, -1):  # 일단 남는자리에 앉히고 조건에 따라 갱신
                # 모든 조건이 동일할 경우 r과 c가 작은 자리에 앉히게 된다.
                seat = (r, c)
            counts = 0
            empty = 0
            for d in range(4):  # 인접한 자리들을 확인
                if 0 <= r+dr[d] < N and 0 <= c+dc[d] < N:
                    if board[r+dr[d]][c+dc[d]] in prefer:
                        counts += 1
                    if not board[r+dr[d]][c+dc[d]]:
                        empty += 1
            if counts > max_counts:  # 선호하는 친구가 많은 자리에 우선 배정
                max_counts = counts
                seat = (r, c)
                max_empty = empty
            elif counts == max_counts:
                if empty > max_empty:  # 같을 경우 빈 자리가 많은 곳에 배정
                    max_empty = empty
                    seat = (r, c)

    board[seat[0]][seat[1]] = student

points = 0
for r in range(N):  # 학생마다 점수를 계산
    for c in range(N):
        student = board[r][c]
        counts = 0
        for d in range(4):
            if 0 <= r + dr[d] < N and 0 <= c + dc[d] < N:
                if board[r + dr[d]][c + dc[d]] in students[student]:
                    # 주변에 선호하는 친구들이 몇명 있는지 확인
                    counts += 1
        if counts:
            points += 10**(counts-1)
print(points)