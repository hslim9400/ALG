
# 그리디
N = int(input())

targets = []
alp_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
alp_dict = {}
firsts = set()
for alp in alp_list:
    alp_dict[alp] = 0
for _ in range(N):
    targets.append(input())

for target in targets:
    for i in range(1, len(target)+1):
        alp_dict[target[-i]] += 10**(i-1)
        if i == len(target):
            firsts.add(target[-i])
alp_list.sort(key=lambda x: alp_dict[x], reverse=True)
pointer = 0
for i in range(9, -1, -1):
    if not alp_dict[alp_list[pointer]]:
        alp_list = alp_list[:pointer]
        break
    alp_dict[alp_list[pointer]] = i
    pointer += 1

if not alp_dict[alp_list[-1]] and alp_list[-1] in firsts:
    pointer = -1
    while True:
        if alp_list[pointer] not in firsts:
            break
        alp_dict[alp_list[pointer]], alp_dict[alp_list[pointer-1]] = alp_dict[alp_list[pointer-1]], alp_dict[alp_list[pointer]]
        pointer -= 1

ans = 0
for target in targets:
    for i in range(1, len(target)+1):
        ans += alp_dict[target[-i]] * (10**(i-1))
print(ans)

