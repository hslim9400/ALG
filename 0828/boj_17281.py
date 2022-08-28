def find_order(order_idx):
    global bat_order, order_list

    if order_idx == 9:
        temp = bat_order[:]
        order_list.append(temp)
        return

    if order_idx == 3:
        find_order(4)
        return

    for i in range(9):
        if visited[i]:
            continue
        bat_order[order_idx] = i
        visited[i] = 1
        find_order(order_idx+1)
        bat_order[order_idx] = 0
        visited[i] = 0


N = int(input())
innings = []
for _ in range(N):
    inning = list(map(int, input().split()))
    innings.append(inning)
max_point = 0
bat_order = [0] * 9
bat_order[3] = 0
visited = [0] * 9
visited[0] = 1
order_list = []
find_order(0)

for bat_order_case in order_list:
    batter = 0
    point = 0
    for inning in range(N):
        bases = []
        outs = 0
        while True:
            bases.append(0)
            hit = innings[inning][bat_order_case[batter]]
            if hit == 0:
                outs += 1
                batter += 1
                batter %= 9
                bases.pop()
                if outs == 3:
                    break
                continue
            for i in range(len(bases) - 1, -1, -1):
                bases[i] += hit
                if bases[i] >= 4:
                    point += len(bases[:i + 1])
                    bases = bases[i + 1:]
                    break
            batter += 1
            batter %= 9
    if point > max_point:
        max_point = point

print(max_point)
