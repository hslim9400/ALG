# CNS 문자열 문제와 너무 유사해서 이거 그리디 안되잖아? 라는 기억으로 완탐을 시도
# => 시간초과가 남
# 이건 그리디로 푸는게 맞다!
# 그때와 다른점은 이 문제는 일단 그리디로 긴 걸 찾아 넣어도 다음 짧은걸 넣었을 때 결과가 같다는 것


S = input()
P = input()

subset = set()
for i in range(len(S)):
    sub_word = ''
    for j in range(i, len(S)):
        sub_word += S[j]
        subset.add(sub_word)
ans = 0
idx = 0
while idx < len(P):
    ans += 1
    for i in range(len(P)-idx, 0, -1):
        if P[idx:idx+i] in subset:
            idx += i
            break
print(ans)