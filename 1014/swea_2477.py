from collections import deque
import heapq


T = int(input())
for test_case in range(1, T+1):
    N, M, K, A, B = map(int, input().split())

    desk_a = [0] + list(map(int, input().split()))
    desk_b = [0] + list(map(int, input().split()))
    clients = deque(list(map(int, input().split())))
    visited = {
        'reception': [0]*(K+1),
        'repair': [0]*(K+1)
    }
    left = K

    reception = [0] * (N+1)
    repair = [0] * (M+1)
    waiting_reception = []
    waiting_repair = []

    t = 0
    client_no = 0

    while True:
        if clients:
            while clients[0] == t:
                client = clients.popleft()
                client_no += 1
                heapq.heappush(waiting_reception, client_no)
                if not clients:
                    break

        for i in range(1, N+1):
            if reception[i]:
                reception[i][0] -= 1
                if reception[i][0] == 0:
                    heapq.heappush(waiting_repair, (t, i, reception[i][1]))
                    reception[i] = 0
            if not waiting_reception:
                continue
            if not reception[i]:
                client = heapq.heappop(waiting_reception)
                reception[i] = [desk_a[i], client]
                visited['reception'][client] = i

        for i in range(1, M+1):
            if repair[i]:
                repair[i][0] -= 1
                if repair[i][0] == 0:
                    repair[i] = 0
            if not waiting_repair:
                continue
            if not repair[i]:
                client = heapq.heappop(waiting_repair)[2]
                repair[i] = [desk_b[i], client]
                visited['repair'][client] = i
                left -= 1
        if not left:
            break

        t += 1

    ans = 0
    for i in range(1, K+1):
        if visited['reception'][i] == A and visited['repair'][i] == B:
            ans += i
    if ans == 0:
        ans = -1
    print(f'#{test_case} {ans}')

