dr = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dc = [0, -1, -1, 0, 1, 1, 1, 0, -1]

def move_cloud(d, s, clouds):  # 구름 옮기기
    new_clouds = set()
    while clouds:  # 구름을 하나씩 뽑아서 넣을 것.
        cloud = clouds.pop()
        r, c = cloud[0], cloud[1]
        nr, nc = r+s*dr[d], c+s*dc[d]  # 지도를 넘어가도 상관 없다. 놀랍게도.
        # N보다 커질 경우 나머지 연산을 하면 당연히 넘어간 만큼 인덱스가 되고
        # 0보다 작을 경우 -1, -2, ..이 되는데 이것도 나머지 연산을 하면
        # 넘어간 만큼 인덱스가 된다.
        nr %= N
        nc %= N
        new_clouds.add((nr, nc))  # 새로운 구름들에 넣어서
    return new_clouds  # 반환


N, M = map(int, input().split())
board = []
for i in range(N):
    line = list(map(int, input().split()))
    board.append(line)

clouds = {(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)}  # 원래 구름들의 자리
for _ in range(M):
    d, s = map(int, input().split())
    clouds = move_cloud(d, s, clouds)  # 구름을 움직이고

    for cloud in clouds:
        board[cloud[0]][cloud[1]] += 1  # 해당 자리들에 물을 1씩 공급

    for cloud in clouds:
        r, c = cloud[0], cloud[1]
        for x, y in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:  # 대각선을 보고
            if 0 <= r+x < N and 0 <= c+y < N:  # 지도 안이라면
                if board[r+x][c+y]:  # 물이 있다면
                    board[r][c] += 1  # 물 복사 버그
    new_clouds = set()
    for i in range(N):
        for j in range(N):  # 지도에
            if board[i][j] >= 2:  # 물이 2 이상 있고
                if (i, j) not in clouds:  # 구름이 있던 자리가 아니라면
                    new_clouds.add((i, j))  # 구름이 된다.
                    board[i][j] -= 2

    clouds = new_clouds  # 새 구름들로 세대교체

water = 0
for i in range(N):  # 남은 물을 세준다.
    for j in range(N):
        water += board[i][j]
print(water)