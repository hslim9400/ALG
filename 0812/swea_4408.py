T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    rooms = []
    for _ in range(N):
        rooms.append(list(map(int, input().split())))
    ways = []
    for i in range(N):
        ways.append([])
        for j in range(2):
            if rooms[i][j] % 2:
                ways[-1].append((rooms[i][j]+1)//2)
            else:
                ways[-1].append(rooms[i][j] // 2)
        ways[-1][0], ways[-1][1] = min(ways[-1]), max(ways[-1])

    hall = [0] * 200
    for i in range(len(ways)):
        for j in range(ways[i][0]-1, ways[i][1]):
            hall[j] = hall[j] + 1

    print(f'#{test_case} {(max(hall))}')
