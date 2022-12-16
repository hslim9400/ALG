

dna = input()
memo = [[0] * len(dna) for _ in range(len(dna))]
# memo[i][j] = i부터 j까지 최대 KOI

for k in range(1, len(dna)):  # k글자 만큼
    for i in range(len(dna) - k):  # i 부터 시작
        memo[i][i+k] = memo[i+1][i+k-1]
        if (dna[i] == 'a' and dna[i+k] == 't') or (dna[i] == 'g' and dna[i+k] == 'c'):
            memo[i][i+k] += 2

        for m in range(1, k+1):
            memo[i][i+k] = max(memo[i][i+k], memo[i][i+k-m] + memo[i+k-m+1][i+k])

print(memo[0][-1])
