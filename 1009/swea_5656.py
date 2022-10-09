from copy import deepcopy

def simulate(depth, board, left):
    global min_left
    if not left:  # 또 다른 종료조건. left가 0일경우 스택에 들어가지 않아 다음총알을 못쏨
        min_left = 0
        return
    if depth == N:  # 최대 네 발 발사하므로 모두 탐색
        if min_left > left:  # 갱신
            min_left = left
        return

    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    for i in range(W):  # 모든 열에 대해 발사해봄
        new_board = deepcopy(board)  # 행렬 복사
        new_left = left  # 값 복사
        stack = []
        for j in range(H):
            if new_board[j][i]:
                stack.append((j, i))  # 해당 열에서 처음으로 맞는 벽돌
                break
        else:
            continue

        while stack:  # 연쇄 폭발을 dfs로 찾아준다.
            current = stack.pop()
            r, c = current
            if not new_board[r][c]:  # 벽돌이 없다면 지나감
                continue
            scope = new_board[r][c]
            current_scope = 0  # 해당 벽돌이 터질때 연쇄로 작용하는 범위
            new_board[r][c] = 0  # 벽돌 깨뜨림
            new_left -= 1  # 벽돌이 깨졌으면 벽돌 수 감소
            while current_scope < scope:  # 범위만큼 연쇄작용
                for d in range(4):
                    nr, nc = r+dr[d]*current_scope, c+dc[d]*current_scope
                    if 0 <= nr < H and 0 <= nc < W:
                        if new_board[nr][nc]:
                            stack.append((nr, nc))
                current_scope += 1
        rotated = list(map(list, zip(*new_board)))  # 아래로 밀기는 어려우니 전치해서
        # 오른쪽으로 밀어주고 다시 전치
        for p in range(W):  # 전치 했으므로 행, 열이 바뀜
            push = []  # 전치 한 녀석이 [0, 2, 0, 0, 1]이라면
            # [0, 0, 0, 2, 1]로 밀어주고 다시 전치할거임
            for q in range(H):
                if rotated[p][q]:  # 0이 아닌 녀석을 세주고
                    push.append(rotated[p][q])
            rotated[p] = [0]*(H-len(push)) + push  # 앞에 0을 붙인다.
        new_board = list(map(list, zip(*rotated)))  # 다시 전치해서
        simulate(depth+1, new_board, new_left)  # 다음 총알 발사


T = int(input())
for test_case in range(1, T+1):
    N, W, H = map(int, input().split())
    board = []
    total = 0  # 처음 벽돌 개수를 세어 줄 것

    for i in range(H):
        line = list(map(int, input().split()))
        board.append(line)
        for j in range(W):
            if line[j]:
                total += 1

    min_left = W * H  # 갱신을 위한 최대가능개수 total로 해도 됨
    simulate(0, board, total)
    print(f'#{test_case} {min_left}')
