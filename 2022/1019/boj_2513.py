N, K, S = map(int, input().split())
lefts = []
rights = []
for _ in range(N):
    info = list(map(int, input().split()))
    if S - info[0] > 0:
        lefts.append(info)
    else:
        rights.append(info)

lefts.sort(key=lambda x: abs(S-x[0]))
rights.sort(key=lambda x: abs(S-x[0]))
total = 0
pointer = len(lefts) - 1
while pointer+1:
    bus = 0
    total += 2 * abs(S - lefts[pointer][0])
    for i in range(pointer, -1, -1):
        if (S - lefts[pointer][0]) * (S - lefts[i][0]) < 0:
            continue
        if bus + lefts[i][1] > K:
            lefts[i][1] -= K - bus
            bus = K
            break
        else:
            bus += lefts[i][1]
            lefts[i][1] = 0
            pointer -= 1

pointer = len(rights) - 1
while pointer+1:
    bus = 0
    total += 2 * abs(S - rights[pointer][0])
    for i in range(pointer, -1, -1):
        if (S - rights[pointer][0]) * (S - rights[i][0]) < 0:
            continue
        if bus + rights[i][1] > K:
            rights[i][1] -= K - bus
            bus = K
            break
        else:
            bus += rights[i][1]
            rights[i][1] = 0
            pointer -= 1

print(total)
