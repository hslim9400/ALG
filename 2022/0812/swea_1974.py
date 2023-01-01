T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    rows = []
    columns = []
    blocks = []
    ans = 1
    for i in range(9):
        row = []
        row = list(map(int, input().split()))
        rows.append(row)

    for j in range(9):
        column = []
        for i in range(9):  # 세로 스도쿠를 확인하기 위해 전치행렬 생성. zip으로 가능
            column.append(rows[i][j])
        columns.append(column)

    for i in range(3):  # 블럭확인을 위해 가로, 세로 3칸마다 블럭 생성
        for j in range(3):
            block = []
            for k in range(3):
                for l in range(3):
                    block.append(rows[3 * i + k][3 * j + l])
            blocks.append(block)

    for i in range(9):  # 만들어 놓은 배열들을 set에 넣고 크기가 0이 아닐 시 답은 0
        if not (len(set(rows[i])) == 9 and len(set(columns[i])) == 9 and len(set(blocks[i])) == 9):
            ans = 0
        if ans == 0:
            break

    print(f'#{test_case} {ans}')