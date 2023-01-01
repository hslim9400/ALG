def snail():  # 달팽이 찍기
    global board
    current = N * N - 1
    r, c = 0, 0
    d = 0
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    while current:
        board[r][c] = current
        if 0 <= r+dr[d] < N and 0 <= c+dc[d] < N and not board[r+dr[d]][c+dc[d]]:
            r += dr[d]
            c += dc[d]
        else:
            d += 1
            d %= 4
            r += dr[d]
            c += dc[d]
        current -= 1


def explode(marbles):  # 구슬이 폭발
    global points
    while True:  # 폭발하는 구슬이 없을 때 까지
        targets = []  # 폭발하는 구슬을 담을 예정
        l = len(marbles)
        start = 0
        counts = 0
        for i in range(1, l):
            if marbles[i] == marbles[i-1]:  # 이어지는 구슬을 카운트
                counts += 1
            else:
                if counts >= 4:
                    targets.append([start, counts])  # start 인덱스 구슬부터 counts개가 터짐
                    start = i
                    counts = 1
                else:
                    start = i
                    counts = 1
        if counts >= 4:
            targets.append([start, counts])  # 마지막을 반영하지 않았음
        if not targets:  # 터질 구슬이 없다면 종료
            return marbles
        pulled = 0  # 인덱스를 당길 숫자.
        for target in targets:
            counts = target[1]
            idx = target[0] - pulled  # start부터 터질건데 pulled만큼 이미 터졌음
            for _ in range(counts):
                points += marbles[idx]  # 점수는 어떤 구슬이 터지는지에 따라
                del marbles[idx]  # 구슬 하나 터짐
            pulled += counts  # 터뜨린 만큼 다음의 인덱스를 당길것임


def transform(marbles):  # 규칙에 따라 변화
    l = len(marbles)
    if l == 1:
        return [0]
    new_marbles = [0] * N**2  # 미리 0으로 된 배열을 만듬
    counts = 1
    pointer = 1  # 어디를 채울지 정하는 포인터
    for i in range(2, l):
        if marbles[i] == marbles[i-1]:  # 이어지는 구슬을 카운트
            counts += 1
        if marbles[i] != marbles[i-1]:  # 구슬 변화
            new_marbles[pointer] = counts  # 몇개가 나왔는지
            pointer += 1
            new_marbles[pointer] = marbles[i-1]  # 무슨 구슬인지
            pointer += 1
            if pointer == N**2:  # 이 이상은 채울 수 없으니 종료
                return new_marbles
            counts = 1
    new_marbles[pointer] = counts  # 이번에도 마지막을 반영하지 않았음
    pointer += 1
    new_marbles[pointer] = marbles[-1]
    for i in range(N**2-1, -1, -1):  # 0 자르기
        if new_marbles[i]:
            new_marbles = new_marbles[:i+1]
            break
    return new_marbles


# 구슬은 1차원 배열에 담아준다.
# 지도에 달팽이를 찍어주고 지도의 해당 위치를 찾아가면
# 구슬 배열의 인덱스로 찾아갈 수 있다.
# 배열은 빈 공간이 없으므로 구슬을 없애면 자동으로 당긴다.

N, M = map(int, input().split())
shark = ((N-1)//2, (N-1)//2)
board = [[0]*N for _ in range(N)]
snail()  # 지도에 구슬 배열의 인덱스를 표기
marbles = [0]*N**2  # 0으로된 배열 생성
for i in range(N):
    line = list(map(int, input().split()))
    for j in range(N):
        marbles[board[i][j]] = line[j]  # 지도를 통해 구슬 배열의 인덱스를 찾아가 기록
for i in range(N**2-1, -1, -1):  # 0 자르기
    if marbles[i]:
        marbles = marbles[:i+1]
        break
else:  
    marbles = [0]

dr = [0, -1, 1, 0, 0]
dc = [0, 0, 0, -1, 1]
points = 0
for _ in range(M):
    d, dist = map(int, input().split())
    for k in range(1, dist+1):  # 거리에 따라 가서 지워줄 것
        r, c = shark[0]+k*dr[d], shark[1]+k*dc[d]  # 상어로부터 정해진 방향으로 k만큼 가서
        idx = board[r][c]  # 보드를 보고 어떤 구슬 배열의 인덱스인지 확인
        if idx-k+1 > len(marbles)-1:  # 찾아갈 수 없는 인덱스
            break
        del marbles[idx-k+1]  # 앞의 k에서 이미 지워줬으니 지운 만큼 인덱스를 당겨 찾아감
    marbles = explode(marbles)  # 터뜨리고
    marbles = transform(marbles)  # 바꾸고
print(points)

