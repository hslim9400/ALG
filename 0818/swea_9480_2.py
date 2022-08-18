def make_set(level, idx, k):
    global words, word_set, word_sets
    if len(word_set) == k:
        word_sets.append(word_set)
        print(word_sets)
        return
    for i in range(idx, N):
        word_set[idx] = words[i]
        make_set(level+1, idx+1, k)


def check(word_sets):
    global count
    for word_set in word_sets:
        target = ''
        for word in word_set:
            target += word
        for alp in alps:
            if alp not in word_set:
                break
        else:
            count += 1


alps = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'
        'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    words = []
    for _ in range(10):
        words.append(input())

    count = 0

    for k in range(1, N+1):
        word_sets = []
        word_set = [0] * k
        make_set(0, 0, k)
        check(word_sets)
    print(count)
