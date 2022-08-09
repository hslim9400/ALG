
T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    dumps = int(input())
    wall = list(map(int, input().split()))
    counts = [0] * 100  # 카운팅정렬을 위해서 만드는 0
    for i in range(100):  # 벽의 넓이는 100으로 고정, 상자 개수는 1에서 100사이
        counts[wall[i]-1] = counts[wall[i]-1] + 1  # 상자의 개수가 1개일 경우 0번째 인덱스

    while True:
        if counts[0] != 0:  # 리스트가 상자의 개수, 값이 상자기둥의 수. 상자기둥이 없는 리스트의 끝쪽은 지운다.
            break
        counts = counts[1:]
    while True:
        if counts[-1] != 0:
            break
        counts = counts[:-1]


    for _ in range(dumps):
        if len(counts) == 1:  # 리스트크기가 한개라면 상자의 높이가 통일되었다는 뜻
            break
        '''
        가장 많이 쌓인 상자에서 하나를 빼서 가장 적게 쌓인 상자에게 하나를 준다.
        카운팅 리스트에선 가장 왼쪽이 가장 많이 쌓인 상자와 가장 적게 쌓인 상자기둥 개수가 하나씩 줄어들고 
        그 안쪽에 기둥개수가 하나씩 늘어난다
        '''
        counts[0], counts[1] = counts[0]-1, counts[1] + 1
        counts[-1], counts[-2] = counts[-1] - 1, counts[-2] + 1

        if counts[0] == 0:  # 만약 가장적게 쌓였던 상자기둥이 유일했다면
            counts = counts[1:]  # 해당 상자 기둥을 없앤다
        if counts[-1] == 0:
            counts = counts[:-1]


    print(f'#{test_case} {len(counts)-1}')