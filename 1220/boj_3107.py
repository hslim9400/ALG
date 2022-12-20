

target = input().split(':')

counts = 8
empty_idx = 0
found = False
empties = []
for i in range(len(target)):
    if target[i] == '':
        if not found:
            empty_idx = i
            found = True
        empties.append(i)
    else:
        counts -= 1
for i in empties[::-1]:
    del target[i]
target = target[:empty_idx] + ['0000']*counts + target[empty_idx:]
for i in range(8):
    target[i] = '0'*(4-len(target[i])) + target[i]

print(':'.join(target))