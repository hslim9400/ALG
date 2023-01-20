
def solution(commands):

    def update_a(r, c, value):
        nonlocal table, original, groups, value_map, current
        group = groups[table[(r, c)][1]]
        for target in group:
            table[target][0] = value
            if value not in value_map.keys():
                value_map[value] = set()
            value_map[value].add(target)
            value_map['EMPTY'].discard(target)

    def update_b(value1, value2):
        nonlocal table, original, groups, value_map, current
        group = value_map[value1]
        for target in group:
            table[target][0] = value2
            if value2 not in value_map.keys():
                value_map[value2] = set()
            value_map[value2].add(target)
        value_map[value1] = set()

    def merge(r_1, c_1, r_2, c_2):
        nonlocal table, original, current, value_map, groups
        # if (r_1, c_1) == (r_2, c_2):
        #     return
        group = min(table[(r_1, c_1)][1], table[(r_2, c_2)][1])
        for target in groups[table[(r_1, c_1)][1]]:
            current[target] = group
            groups[group].add(target)
            table[target][2] = group
        for target in groups[table[(r_2, c_2)][1]]:
            current[target] = group
            groups[group].add(target)
            table[target][2] = group

        if table[(r_1, c_1)][0] != 'EMPTY':
            update_a(r_2, c_2, table[(r_1, c_1)][0])
        elif table[(r_2, c_2)][1] != 'EMPTY':
            update_a(r_1, c_1, table[(r_2, c_2)][0])

    def unmerge(r, c):
        nonlocal table, original, current, value_map, groups
        group = set(groups[table[(r, c)][1]])
        value = table[(r, c)][0]
        for target in group:
            table[target][0] = 'EMPTY'
            current[target] = original[target]
            groups[current[target]] = {target}
            value_map['EMPTY'].add(target)
        table[(r, c)][0] = value
        value_map[value] = {(r, c)}
        value_map['EMPTY'].discard((r, c))

    answer = []
    table = {}
    original = {}
    current = {}
    groups = {}
    value_map = {'EMPTY': set()}
    count = 1
    for i in range(51):
        for j in range(51):
            table[(i, j)] = ["EMPTY", count]
            original[(i, j)] = count
            current[(i, j)] = count
            groups[count] = {(i, j)}
            value_map['EMPTY'].add((i, j))
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
            answer.append(table[(int(command[1]), int(command[2]))][1])

    return answer
