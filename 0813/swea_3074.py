T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    people = M
    control = []
    for _ in range(N):
        control.append(int(input()))

    min_time = 1
    max_time = max(control) * M
    while min_time <= max_time:
        guess = (min_time + max_time) // 2
        finish = 0
        for time in control:
            finish += guess // time
            if finish >= people:
                max_time = guess - 1
                break
        if finish < people:
            min_time = guess + 1
    print(f'#{test_case} {guess+1}')
