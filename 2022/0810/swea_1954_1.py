def next_num(n, snail, index, direction):
    i, j = index[0], index[1]
    if direction == 'right':
        snail[i][j + 1] = str(n)
        index = [i, j + 1]
        if j + 1 == N - 1:
            direction = 'down'
        elif snail[i][j + 2] != ' ':
            direction = 'down'
    elif direction == 'down':
        snail[i + 1][j] = str(n)
        index = [i + 1, j]
        if i + 1 == N - 1:
            direction = 'left'
        elif snail[i + 2][j] != ' ':
            direction = 'left'
    elif direction == 'left':
        snail[i][j - 1] = str(n)
        index = [i, j - 1]
        if j - 1 == 0:
            direction = 'up'
        elif snail[i][j - 2] != ' ':
            direction = 'up'
    elif direction == 'up':
        snail[i - 1][j] = str(n)
        index = [i - 1, j]
        if i - 1 == 0:
            direction = 'right'
        elif snail[i - 2][j] != ' ':
            direction = 'right'

    return snail, index, direction


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())
    last = N ** 2
    snail = []
    for i in range(N):
        snail.append([])
        for j in range(N):
            snail[-1].append(' ')

    snail[0][0] = '1'
    direction = 'right'
    index = [0, 0]

    if N != 1:
        for n in range(2, last + 1):
            snail, index, direction = next_num(n, snail, index, direction)

    print(f'#{test_case}')
    for i in range(N):
        print(' '.join(snail[i]))

    # ///////////////////////////////////////////////////////////////////////////////////