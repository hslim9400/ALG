T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    case, N = input().split()
    N = int(N)
    nums = list(range(10))  # 0부터 9까지의 숫자리스트
    alien = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']  # 0부터 9까지 외계어리스트
    signal = input().split()
    trans = []  # 변환된 것을 담을 리스트
    decoder = {}  # 서로 변환하게 할 딕셔너리

    for i in range(10):  # 숫자와 외계어를 매칭할 딕셔너리 생성
        decoder[nums[i]] = alien[i]
        decoder[alien[i]] = nums[i]

    for i in range(N):  # 외계어를 숫자로 변환해 리스트에 저장
        trans.append(decoder[signal[i]])

    trans.sort()  # 리스트를 정렬
    for i in range(N):  # 숫자를 외계어로 변환
        trans[i] = decoder[trans[i]]

    print(case)
    print(*trans)  # 애스터리스크로 언패킹하여 출력
