def powerset(idx):
    global ans
    if idx == 10:  # 끝까지 내려가서
        subset = []
        for j in range(10):
            if check[j] == 1:  # 체크를 확인
                subset.append([num_set[j]])  # 부분집합에 살아있는 숫자들 추가
        ans.append(subset)  # 부분집합 추가
        return
    check[idx] = 0  # 해당 숫자가 없을 것
    powerset(idx + 1)
    check[idx] = 1  # 해당 숫자가 있을 것
    powerset(idx + 1)


num_set = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
check = [0] * 10
ans = []
powerset(0)

print(ans)
