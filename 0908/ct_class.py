class number:
    def __init__(self, value, idx):
        self.value = value
        self.idx = idx


N = int(input())
num_list = list(map(int, input().split()))

new_list = []
for i in range(N):
    new_list.append(number(num_list[i], i))
clone = new_list[:]
clone.sort(key = lambda x: (x.value, x.idx))

ans = []
for number1 in new_list:
    for i in range(N):
        if number1 == clone[i]:
            ans.append(i+1)
print(*ans)
