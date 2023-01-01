
N = int(input())
scores = list(map(int, input().split()))
points = [0] * len(scores)  # DP용 배열 n번째 멤버가 들어올 경우 조가 잘 짜여진 정도의 최댓값
points[0] = 0
if len(scores) > 1:
    points[1] = abs(scores[1] - scores[0])  # 두 명이 한 조니까 두 명의 차이

if len(scores) > 2:
    current = scores[:3]  # 세 명도 한 조가 좋으니 최댓값 - 최솟값
    current_diff = max(current) - min(current)  # 차이를 저장
    points[2] = current_diff

    for i in range(3, len(scores)):
        new = scores[i]  # 새로 온 친구
        prev = scores[i-1]  # 하나 전
        current.append(new)  # 일단 현재 조에 투입
        if points[i-2] + abs(new - prev) > points[i-1] + (max(current) - min(current) - current_diff):
            # current_diff는 원래 조의 최댓갑-최솟값의 차이인데
            # 새로 조를 만들었을 때 더해지는 점수 > 원래 조에 넣어줬을때의 점수 라면
            # 조를 새로 만들어 준다.
            points[i] = points[i-2] + abs(new - prev)
            current = [prev, new]
            current_diff = abs(new - prev)
        else:
            # 아니라면 원래 조에 넣고 최댓값-최솟값 차이를 갱신
            points[i] = points[i-1]
            if max(current) - min(current) > current_diff:
                points[i] = points[i-1] + max(current) - min(current) - current_diff
                current_diff = max(current) - min(current)

print(points[-1])
