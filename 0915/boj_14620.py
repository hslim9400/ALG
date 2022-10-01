N = int(input())
board = []
for i in range(N):
    board.append(list(map(int, input().split())))
min_price = N*N*200
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
# 공포의 7중포문 
# 꽃 세개의 좌표를 모두 탐색한다.
for x1 in range(1, N-1):
    for y1 in range(1, N-1):
        for x2 in range(1, N-1):
            for y2 in range(1, N-1):
                if (x1, y1) == (x2, y2):  # 겹치면 안됨
                    continue
                for x3 in range(1, N-1):
                    for y3 in range(1, N-1):
                        if (x2, y2) == (x3, y3) or (x1, y1) == (x3, y3):  # 하나라도 겹치면 안됨
                            continue
                        targets = {(x1,y1), (x2,y2), (x3,y3)}  # 꽃잎도 겹치면 안됨
                        for d in range(4):  # 꽃 잎 생성
                            targets.add((x1 + dx[d], y1 + dy[d]))
                            targets.add((x2 + dx[d], y2 + dy[d]))
                            targets.add((x3 + dx[d], y3 + dy[d]))
                        if len(targets) != 15:  # 겹치면 셋에 중복해서 들어갈 수 없을 것
                            break
                        price = 0
                        for target in targets:  # 가격 정산
                            price += board[target[0]][target[1]]
                            if price > min_price:
                                break
                        if price < min_price:  # 최솟값 갱신
                            min_price = price
print(min_price)