T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    print(f'#{test_case}')
    line = [1]  # 처음으로 출력할 1행
    for i in range(N):
        print(*line)  # 저장되어있는 행을 출력한다
        new_line = line[:]
        line = line + [0]  # 현재 행에 0을 추가하고
        for i in range(len(new_line)):  # 자신을 한칸씩 오른쪽으로 밀어 더하면 다음행이 완성된다.
            line[i+1] += new_line[i]  # [1 3 3 1 0] 에 [1 3 3 1]을 더해주면 [1 4 6 4 1]
