T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    cheese = list(map(int, input().split()))  # 치즈들의 리스트
    for i in range(M):
        cheese[i] = [cheese[i], i+1]  # 치즈들에게 번호를 매겨준다. 첫 번째 치즈가 1번
    queue = []
    for i in range(N):  # 일단 화덕에 피자들을 채운다.
        queue.append(cheese.pop(0))

    while len(queue) > 1:  # 화덕에 피자가 하나만 남았다면 종료
        current = queue.pop(0)  # 가장 앞의 피자를 꺼내서 
        current[0] = current[0]//2  # 치즈가 한번에 녹았다고 치고
        if current[0] == 0:  # 치즈가 모두 녹았다면
            if cheese:  # 화덕밖에 남은 피자가 있다면
                queue.append(cheese.pop(0))  # 화덕에 넣어준다.
            continue
        queue.append(current)  # 치즈가 모두 녹지 않았다면 화덕에 다시 넣는다.

    print(f'#{test_case} {queue[0][1]}')
