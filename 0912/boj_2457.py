

N = int(input())
flowers = []
for i in range(N):
    start_m, start_d, end_m, end_d = map(int, input().split())
    if end_m == 1 or end_m == 2 or start_m == 12:
        continue
    # 전처리로 1,2월에 피는건 3월1일에 피도록, 12월에 지는 꽃은 11월 30일에 지도록 한다.
    if start_m == 1 or start_m == 2:
        start_m = 3
        start_d = 1
    if end_m == 12:
        end_m = 12
        end_d = 1
    flowers.append((start_m, start_d, end_m, end_d))

flowers.sort(key=lambda x: (x[0], x[1]))
start = [3, 1]
picked = []
flag = True
ans = 0
while flag:
    cands = []
    while True:
        # cands에 꽃들 추가하는 과정, 이전 꽃이 지기 전에 피는 꽃들을 추가
        if not flowers:
            break
        flower = flowers[0]
        if flower[0] < start[0]:
            cands.append(flowers.pop(0))
        elif flower[0] == start[0] and flower[1] <= start[1]:
            cands.append(flowers.pop(0))
        else:
            break
    if not cands:
        # 그런 꽃들이 없다면 틀렸다.
        break
    # 가장 늦게 지는 꽃을 고른다.
    cands.sort(key=lambda x: (x[2], x[3]))
    picked.append(cands[-1])
    # 추가한 꽃이 11월 30일까지 폈다면 종료
    if picked[-1][2] == 12 and picked[-1][3] == 1:
        ans = len(picked)
        break
    # 다음 꽃들이 피는 시점의 조건을 갱신
    start[0] = picked[-1][2]
    start[1] = picked[-1][3]
    # 꽃들이 없다면 종료
    if not flowers:
        break
print(ans)
