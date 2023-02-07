
def solution(commands):
    # 문제에서 구현하라는 명령어들을 구현
    # 표의 크기는 50 * 50이고
    # 명령어의 크기는 1000개 이므로
    # 명령어마다 모든 칸을 탐색해도 시간초과날 일이 없다
    def update_a(r, c, value):
        # (r, c)와 같은 그룹의 칸을 업데이트
        group = table[r][c][1]
        for i in range(1, 51):
            for j in range(1, 51):
                if table[i][j][1] == group:
                    table[i][j][0] = value

    def update_b(value1, value2):
        # 값이 value1인 칸들을 모두 value2로 업데이트
        for i in range(1, 51):
            for j in range(1, 51):
                if table[i][j][0] == value1:
                    table[i][j][0] = value2

    def merge(r_1, c_1, r_2, c_2):
        # (r1, c1)그룹과 (r2, c2)그룹을 병합
        # 기준은 내 마음대로 선택(min)
        group = min(table[r_1][c_1][1], table[r_2][c_2][1])
        groups = (table[r_1][c_1][1], table[r_2][c_2][1])
        for i in range(1, 51):
            for j in range(1, 51):
                # 두 그룹중 하나에 속한다면 더 작은 그룹으로 병합
                if table[i][j][1] in groups:
                    table[i][j][1] = group
        # 그룹을 병합했으니 값을 업데이트
        if table[r_1][c_1][0]:
            update_a(r_2, c_2, table[r_1][c_1][0])
        elif table[r_2][c_2][0]:
            update_a(r_1, c_1, table[r_2][c_2][0])

    def unmerge(r, c):
        # 병합 해제
        # 값과 그룹을 초기화
        group = table[r][c][1]
        value = table[r][c][0]
        for i in range(1, 51):
            for j in range(1, 51):
                if table[i][j][1] == group:
                    table[i][j][1] = original[i][j]
                    table[i][j][0] = 0
        table[r][c][0] = value

    answer = []
    table = [[[0, 0]] * 51 for _ in range(51)]
    # table : [현재 값, 현재 그룹]으로 구성된 리스트
    original = [[0] * 51 for _ in range(51)]
    # 초기화를 위한 처음 그룹
    count = 1
    for i in range(1, 51):
        for j in range(1, 51):
            table[i][j] = [0, count]
            original[i][j] = count
            count += 1

    for command in commands:
        command = command.split()
        if command[0] == 'UPDATE':
            if len(command) == 4:
                update_a(int(command[1]), int(command[2]), command[3])
            else:
                update_b(command[1], command[2])
        if command[0] == 'MERGE':
            merge(int(command[1]), int(command[2]), int(command[3]), int(command[4]))
        if command[0] == 'UNMERGE':
            unmerge(int(command[1]), int(command[2]))
        if command[0] == 'PRINT':
            if table[int(command[1])][int(command[2])][0]:
                answer.append(table[int(command[1])][int(command[2])][0])
            else:
                answer.append("EMPTY")

    return answer
