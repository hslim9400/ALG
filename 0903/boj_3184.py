r, c = map(int, input().split())
areas = [[]]
garden = []
for i in range(r):
    line = list(input())
    garden.append(line)
    for j in range(c):
        if line[j] != '#':
            for area in areas:
                if (i-1, j) in area or (i, j-1) in area:
                    area.append((i, j))
                    break
            else:
                areas.append([(i, j)])

print(len(areas))
while True:
    flag = False
    for area1 in areas:
        for area2 in areas:

    else:
        break
print(len(areas))

survived = [0, 0]
for area in areas:
    sheep = 0
    wolf = 0
    for coord in area:
        if garden[coord[0]][coord[1]] == 'o':
            sheep += 1
        if garden[coord[0]][coord[1]] == 'v':
            wolf += 1
    if sheep > wolf:
        survived[0] += sheep
    else:
        survived[1] += wolf
print(*survived)

