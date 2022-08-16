T = int(input())
for test_case in range(1, T+1):
    A, B = input().split()
    count_B = A.count(B)  # A에 B가 몇개 들어있는지 확인
    ans = len(A) - (len(B) * count_B) + count_B  # B를 한번만 누르면 B의 길이만큼의 문자열이 입력된다.

    print(f'#{test_case} {ans}')
