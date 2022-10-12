def choose(depth, current_stairs):
    # 모든 사람이 두 계단을 선택하는 모든 경우를 탐색 할 예정
    global min_time
    if depth == len(people):
        end = 0
        for stair in current_stairs.keys():
            if not current_stairs[stair][1]:  # 아무도 해당 계단을 선택하지 않음
                continue
            current_stairs[stair][1].sort()  # 계단에 도착 하는 시간들을 정렬
            queue = []  # 계단을 이용중인 사람들이 들어감
            for i in range(len(current_stairs[stair][1])):
                arrive = current_stairs[stair][1][i]  # 사람 한 명이 계단에 도착한 시간
                if len(queue) == 3:  # 최대 세명이 이용하므로 다음 사람은 첫 사람이 나가는 것을 기다림
                    leave = queue.pop(0)  # 나가는 시간
                    queue.append(max(leave, arrive+1)+current_stairs[stair][0])  # 애초에 사람이 나갈 시간을 넣음
                    # 도착시간+1초, 첫 사람이 나가는 시간 중 늦은 시간 + 계단을 이용하는 시간
                else:  # 계단을 이용하는 사람이 2명이하면 그냥 계단을 이용
                    queue.append(arrive+current_stairs[stair][0]+1)
            if end < queue[-1]:  # 마지막으로 들어온 사람이 나가는 시간이 해당 계단선택조합의 소요시간이 됨
                end = queue[-1]
                if end > min_time:  # 백트래킹, 이미 갱신할 수 없는 조합
                    break
        if min_time > end:
            min_time = end
        return

    person = people[depth]  # 지금 계단을 선택 할 사람
    for stair in current_stairs.keys():  # 두개의 계단 중 한개를 선택해 다음 사람에게 간다.
        current_dist = abs(person[0]-stair[0]) + abs(person[1]-stair[1])
        current_stairs[stair][1].append(current_dist)
        choose(depth+1, current_stairs)
        current_stairs[stair][1].remove(current_dist)


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    board = []
    stairs = {}
    people = []
    for i in range(N):
        line = list(map(int, input().split()))
        board.append(line)
        for j in range(N):
            if line[j] > 1:
                stairs[(i, j)] = [line[j], []]
            if line[j] == 1:
                people.append((i, j))

    min_time = float('inf')
    choose(0, stairs)
    print(f'#{test_case} {min_time}')
