
T = int(input())
for test_case in range(1, T+1):
    n, q = map(int, input().split())

    houses = []
    house_dict = {}
    for i in range(n):
        line = list(map(int, input().split()))
        line.append(i)
        line.append(0)
        line.append(0)
        houses.append(line)
        house_dict[i] = [line[2], 0, 0]
    houses.sort(key=lambda x: (x[0]+x[1], x[0]))
    houses_m = sorted(houses, key=lambda x: (-x[2], x[3]))

    events = []
    for i in range(q):
        line = list(map(int, input().split()))
        events.append(line)
    events.sort(key = lambda x: x[1])

    current = 0
    cv = []
    for event in events:
        t = event[1]
        for house in houses:
            house_no = house[3]
            if house_dict[house_no][1] <= t - current:
                house_dict[house_no][1] = 0
            else:
                house_dict[house_no][1] -= t - current
        current = t

        if event[0] == 1:
            for house in houses:
                house_no = house[3]
                if house_dict[house_no][1] == 0:
                    house_dict[house_no][1] = 2 * (house[0]+house[1])
                    house_dict[house_no][2] += event[2]
                    break
            else:
                cv.append(event[2])
                cv.sort(reverse=True)
        else:
            while cv:
                for house in houses:
                    house_no = house[3]
                    if house_dict[house_no][1] == 0:
                        house_dict[house_no][1] = 2 * (house[0] + house[1])
                        house_dict[house_no][2] += cv.pop(0)
                        break
                else:
                    break
            for house in houses_m:
                house_no = house[3]
                if house_dict[house_no][1] == 0:
                    if event[3] > house_dict[house_no][0]:
                        break

                    dist = abs(event[4]-house[0]) + abs(event[5]-house[1])
                    house_dict[house_no][1] = 2 * dist
                    house_dict[house_no][2] += event[2]
                    house_dict[house_no][0] -= event[3]
                    break

    ans = []
    for i in range(n):
        ans.append(house_dict[i][2])

    print(f'#{test_case}', *ans)
