# 트리경로를 따라 이동하며 양이 다 먹히거나 1에 도착해서 더 움직이지 않는다면
# 해당 양들의 출발점과 도착점을 이어버린다.

N = int(input())
islands = [0] * (N+1)
sheeps = [0] * (N+1)
wolves = [0] * (N+1)
starts = []

for i in range(2, N+1):
    t, a, p = input().split()
    if t == 'S':
        sheeps[i] = int(a)
        starts.append(i)
    else:
        wolves[i] = int(a)
    islands[i] = int(p)

stop = 0
for i in range(len(starts)):  # 시작점들을 한번씩만 순회
    start = starts[i]  # 시작점을 저장
    sheep = sheeps[start]  # 출발하는 양들
    current = start  # 끝 점이 될 값
    while sheep and current != 1:  # 양이 모두 먹히거나 1에 도착하면 반복문 종료
        if islands[current]:  # 지금 생각하니 필요없는 코드
            current = islands[current]  # 한칸 전진
            if wolves[current]:  # 늑대가 있다면 계산
                if sheep >= wolves[current]:
                    sheep -= wolves[current]
                    wolves[current] = 0
                else:
                    wolves[current] -= sheep
                    sheep = 0
    islands[start] = current  # 저장했던 시작점과 끝점을 잇는다.
    if current == 1:  # 도착점이 1이라면 양들을 더해준다.
        sheeps[1] += sheep

print(sheeps[1])