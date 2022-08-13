T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    rooms = []
    for _ in range(N):
        rooms.append(list(map(int, input().split())))
    ways = []
    for i in range(N):
        ways.append([])
        for j in range(2):  # 학생들이 움직일 방을 복도로 바꾸어 저장
            if rooms[i][j] % 2:  # 짝수 방은 2로 나누고 홀수는 1을 더해서 2로 나누면
                ways[-1].append((rooms[i][j]+1)//2)
            else:  # 1,2는 1번복도, 3, 4는 2번복도 이런식으로 저장됨
                ways[-1].append(rooms[i][j] // 2)
        ways[-1][0], ways[-1][1] = min(ways[-1]), max(ways[-1])
        # 복도 중 작은 값이 0번인덱스, 큰 값이 1번 인덱스가 된다.

    hall = [0] * 200  # 200칸짜리 복도를 생성
    for i in range(len(ways)):
        for j in range(ways[i][0]-1, ways[i][1]):  # 복도를 밟는다면 해당 칸 + 1
            hall[j] = hall[j] + 1

    print(f'#{test_case} {(max(hall))}')
