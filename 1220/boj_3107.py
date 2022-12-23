# ':'를 기준으로 문자열들을 나누고, 4글자가 되도록 0을 채워주면 
# 일반적인 경우는 어렵지 않다.
# 다만, ::가 숫자들 가운데 있는지, 양측 끝에 있는지에 따라 다르게 풀어야 할 수 있다.

# 이 풀이는 빈칸의 인덱스를 저장해두고 그 곳에는 숫자가 없는 만큼의 '0000'을 채우고
# 빈 칸을 모두 지운 후 위의 알고리즘을 적용했다.

target = input().split(':')

counts = 8
empty_idx = 0
found = False
empties = []
for i in range(len(target)):
    if target[i] == '':
        if not found:
            empty_idx = i  # '0000'이 들어갈 인덱스를 저장
            found = True
        empties.append(i)  # 빈 칸을 지우기 위해 인덱스를 모은다.
    else:
        counts -= 1
for i in empties[::-1]:
    del target[i]  # 빈 칸을 지운다.

target = target[:empty_idx] + ['0000']*counts + target[empty_idx:]
# 들어갈 자리에 '0000'을 삽입
for i in range(8):
    target[i] = '0'*(4-len(target[i])) + target[i]

print(':'.join(target))