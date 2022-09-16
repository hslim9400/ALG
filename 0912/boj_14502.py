def remove_area():  # dfs로 감염된 지역 없애기
    global areas, max_safe_zone
    stack = virus[:]  # 감염 시작지 스택에 추가
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    visited = set()
    while stack:
        current = stack.pop()
        if current in visited:
            continue
        visited.add(current)
        r = current[0]
        c = current[1]
        for d in range(4):
            if (r+dr[d], c+dc[d]) in areas and (r+dr[d], c+dc[d]) not in visited:
                stack.append((r+dr[d], c+dc[d]))
    for area in visited:  # visited에 있다면 감염되는 지역
        areas.discard(area)
    safe_zone = len(areas)  # 감염되지 않는 지역의 개수
    if safe_zone > max_safe_zone:  # 최댓값 갱신
        max_safe_zone = safe_zone
    for area in visited:  # 연구소 초기화
        areas.add(area)


N, M = map(int, input().split())
areas = set()
walls = []
virus = []
for i in range(N):
    line = list(map(int, input().split()))
    for j in range(M):
        if line[j] != 1:
            areas.add((i,j))
        if line[j] == 0:
            walls.append((i,j))
        if line[j] == 2:
            virus.append((i,j))

w = len(walls)
max_safe_zone = 0
for i in range(w-2):  # 재귀보다 빠른 포문으로 조합찾기
    for j in range(i+1, w-1):
        for k in range(j+1, w):
            areas.remove(walls[i])  # 벽 설치
            areas.remove(walls[j])
            areas.remove(walls[k])
            remove_area()  # 감염되지 않는 지역 찾기
            areas.add(walls[i])  # 벽 허물기
            areas.add(walls[j])
            areas.add(walls[k])
print(max_safe_zone)