def drive(depth, battery, counts):
    global min_counts
    if depth == N-1:

        if counts < min_counts:
            min_counts = counts
        return

    if battery > 0:
        drive(depth+1, battery-1, counts)
    if counts < min_counts-1:
        drive(depth+1, stations[depth]-1, counts+1)


T = int(input())

for test_case in range(1, T+1):
    info = list(map(int, input().split()))
    N = info[0]
    stations = info[1:]
    min_counts = N
    drive(0, 0, -1)
    print(f'#{test_case} {min_counts}')
