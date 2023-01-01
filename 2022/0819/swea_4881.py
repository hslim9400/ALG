
def next_row(row, prev_sum):  # 다음 줄을 확인하는 함수, 지금까지의 합을 가지고 내려간다.
    global visited, min_sum
    new_sum = prev_sum
    if row == N-1:  # 마지막 줄에 도달
        for i in range(N):
            if i not in visited:  # 아직 더하지 않은 열을 확인해 더한다.
                new_sum += board[row][i]
        if min_sum > new_sum:  # 최솟값이라면 갱신
            min_sum = new_sum
        return

    for i in range(N):
        new_sum = prev_sum  # 합을 조작하기 위해 값을 복사
        if i in visited:  # 중복을 피하기 위해 마킹을 확인
            continue
        new_sum += board[row][i]
        if new_sum > min_sum:  # 백트래킹 조건, 더하다가 최솟값보다 커지면 버리고 돌아간다.
            continue
        visited.append(i)  # 방문 한 곳에 i를 추가하고
        next_row(row+1, new_sum)  # 내려보낸 후
        visited.remove(i)  # 위의 함수가 끝나면 초기화


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    board = []
    for _ in range(N):
        board.append(list(map(int, input().split())))
    min_sum = 9 * N  # 가능한 최대 합. 첫 탐색때 갱신 할 것
    visited = []
    next_row(0, 0)

    print(f'#{test_case} {min_sum}')

