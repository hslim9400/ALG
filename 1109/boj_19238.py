from collections import deque
import heapq


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
    min_dist = N*N
    targets = []
    for customer in customers:
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
        ans = -1
        break
    target = heapq.heappop(targets)
    taxi = (target[0], target[1])
    fuel -= min_dist
    destination = (target[2], target[3])
    destination_dist = get_dist(taxi, destination)
    if destination_dist == -1 or destination_dist > fuel:
        ans = -1
        break
    taxi = destination
    fuel += destination_dist
    customers.remove(target)
if not ans:
    ans = fuel
print(ans)
