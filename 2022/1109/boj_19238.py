from collections import deque
import heapq
# 사용한 자료구조:
# board : 길과 벽의 2차원 배열
# customers : 손님의 위치, 목적지가 담긴 배열
# targets : 택시로 부터 같은 거리의 손님들을 담을 힙(행, 열을 기준으로 힙이 구성됨)


# 택시와 목적지 사이의 거리를 구하는 bfs함수
# 목적지를 인자로 넣어야 하기 때문에 아래의 문제가 발생했음.
def get_dist(taxi, target):
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    queue = deque()
    queue.append((taxi[0], taxi[1], 0))
    visited = set()
    while queue:
        r, c, dist = queue.popleft()
        if (r, c) in visited:
            continue
        visited.add((r, c))
        if (r, c) == target:
            return dist
        for d in range(4):
            nr, nc = r+dr[d], c+dc[d]
            if 0 <= nr < N and 0 <= nc < N and not board[nr][nc] and (nr, nc) not in visited:
                queue.append((nr, nc, dist+1))
    return -1


N, M, fuel = map(int, input().split())
board = []
for _ in range(N):
    line = list(map(int, input().split()))
    board.append(line)

x, y = map(int, input().split())
taxi = (x-1, y-1)
customers = []
for _ in range(M):
    r_1, c_1, r_2, c_2 = list(map(int, input().split()))
    customers.append([r_1-1, c_1-1, r_2-1, c_2-1])
ans = 0
while customers:
    # 모든 손님을 운반한다면 종료
    min_dist = N*N
    targets = []
    for customer in customers:
        # 택시와 목적지 사이의 거리를 구하는 함수를 만들었기 때문에 
        # 손님 한 명마다 각각 bfs 실행하고 있었다.
        # 그냥 택시에서 bfs를 한번 실행해서 만나는 손님들을 targets에 담도록 구현하는게 좋음
        # 백트래킹을 해주니 이 로직도 시간안에 돌아가긴 한다.
        if abs(customer[0] - taxi[0]) + abs(customer[1] - taxi[1]) > min_dist \
                or abs(customer[0] - taxi[0]) + abs(customer[1] - taxi[1]) > fuel:
            continue
        customer_location = (customer[0], customer[1])
        temp_dist = get_dist(taxi, customer_location)
        if temp_dist != -1:
            if temp_dist < min_dist:
                targets = [customer]
                min_dist = temp_dist
            if temp_dist == min_dist:
                heapq.heappush(targets, customer)
    if not targets or min_dist > fuel:
        # 택시가 손님에게 갈 수 없거나 연료가 모자라다면 종료
        ans = -1
        break
    target = heapq.heappop(targets)
    # 힙이기 때문에 조건에 맞는 손님이 튀어나옴
    taxi = (target[0], target[1])
    fuel -= min_dist
    destination = (target[2], target[3])
    destination_dist = get_dist(taxi, destination)
    if destination_dist == -1 or destination_dist > fuel:
        # 택시가 목적지에 갈 수 없거나 연료가 모자라다면 종료
        ans = -1
        break
    taxi = destination
    fuel += destination_dist
    customers.remove(target)
if not ans:
    ans = fuel
print(ans)
