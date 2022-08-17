V, E = 7, 8
edge_list = list(map(int, input().split()))
adj = [[0]*8 for _ in range(8)]  # 인접행렬을 만들기 위한 빈 행렬
for i in range(8):  # 입력받은 정보로 인접행렬을 생성
    start = edge_list[2*i]
    end = edge_list[2*i + 1]
    adj[start][end] = 1
    adj[end][start] = 1  # 방향이 없으므로 연걸되어 있다면 end-start도 연결해준다.

stack = [1]
visited = []
while stack:  # stack이 비면 종료
    current = stack.pop()
    if current in visited:  # 이미 방문했다면 그냥 지나간다.
        continue
    visited.append(current)
    for destination in range(8):  # 현위치에서 갈 수 있는 곳을 찾고, 방문했는지도 확인
        if adj[current][destination] and destination not in visited:
            stack.append(destination)

print(visited)