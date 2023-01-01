# 냅색알고리즘과 유사함
# memo[i][j]는 dna의 i번째 글자부터 j번째 글자까지 중 최대 KOI
# 'at', 'gc'로 감싸져 있는 경우 2를 더해주고
# 둘로 나눠 만들 수 있는 KOI 중 가장 큰 값으로 갱신해준다.

dna = input()
memo = [[0] * len(dna) for _ in range(len(dna))]
# memo[i][j] = i부터 j까지 최대 KOI

for k in range(1, len(dna)):  # k글자 만큼
    for i in range(len(dna) - k):  # i 부터 시작
        memo[i][i+k] = memo[i+1][i+k-1]
        if (dna[i] == 'a' and dna[i+k] == 't') or (dna[i] == 'g' and dna[i+k] == 'c'):
            memo[i][i+k] += 2

        for m in range(1, k+1):
            # 어떤 부분문자열을 m개를 기준으로 두개로 나눠 가능한 가장 큰 값으로 갱신.
            memo[i][i+k] = max(memo[i][i+k], memo[i][i+k-m] + memo[i+k-m+1][i+k])

print(memo[0][-1])  # 0부터 끝까지 글자로 만들 수 있는 최대 KOI가 출력됨
