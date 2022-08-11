T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    ans = []  # 답으로 출력할 리스트

    for i in range(len(nums)//2):
        ans.append(nums.pop(nums.index(max(nums))))  # 봉인 해제 된 내장함수
        ans.append(nums.pop(nums.index(min(nums))))  # 최대, 최소값의 인덱스를 찾아 원래 리스트에서 빼서 정답리스트에 넣는다.

    ans = ans[:10]  # 열개만 출력하므로 자른다
    print(f'#{test_case}', *ans)