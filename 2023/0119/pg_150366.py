
def solution(commands):

    def update_a(r, c, value):
        group = table[r][c][1]
        for i in range(1, 51):
            for j in range(1, 51):
                if table[i][j][1] == group:
                    table[i][j][0] = value

    def update_b(value1, value2):
        for i in range(1, 51):
            for j in range(1, 51):
                if table[i][j][0] == value1:
                    table[i][j][0] = value2

    def merge(r_1, c_1, r_2, c_2):
        group = min(table[r_1][c_1][1], table[r_2][c_2][1])
        groups = (table[r_1][c_1][1], table[r_2][c_2][1])
        for i in range(1, 51):
            for j in range(1, 51):
                if table[i][j][1] in groups:
                    table[i][j][1] = group
        if table[r_1][c_1][0]:
            update_a(r_2, c_2, table[r_1][c_1][0])
        elif table[r_2][c_2][0]:
            update_a(r_1, c_1, table[r_2][c_2][0])

    def unmerge(r, c):
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
    original = [[0] * 51 for _ in range(51)]
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
