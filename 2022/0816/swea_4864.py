# 문자열 비교
T = int(input())
for test_case in range(1, T+1):
    str_1 = input()
    str_2 = input()
    ans = 0
    if str_1 in str_2:  # 있다면 답이 1
        ans = 1
    print(f'#{test_case} {ans}')
