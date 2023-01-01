T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    schedules = []
    for _ in range(N):
        start, end = map(int, input().split())
        schedules.append((start, end))

    schedules.sort(key= lambda x: (x[1], x[0]))

    day = [(0,0)]
    for schedule in schedules:
        last = day[-1]
        if schedule[0] >= last[1]:
            day.append(schedule)

    print(f'#{test_case} {len(day)-1}')
