
R, C = map(int, input().split())
words = []
for i in range(R):
    words.append(input())

idxs = list(range(C))
ans = R-1
strings = {}
while ans:
    new_strings = {}
    for i in idxs:
        if strings:
            base = strings[i]
        else:
            base = ''
        if base+words[ans][i] in new_strings.keys():
            new_strings[base+words[ans][i]].append(i)
        else:
            new_strings[base+words[ans][i]] = [i]
    idxs = []
    strings = {}
    for made_word in new_strings.keys():
        if len(new_strings[made_word]) > 1:
            idxs.extend(new_strings[made_word])
            for idx in new_strings[made_word]:
                strings[idx] = made_word
    if not idxs:
        break
    ans -= 1
print(ans)


