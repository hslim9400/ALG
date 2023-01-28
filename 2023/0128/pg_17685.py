def solution(words):
    answer = 0
    trie = {'counts': 0}
    for word in words:
        current = trie
        current['counts'] += 1
        for letter in word:
            if letter not in current.keys():
                current[letter] = {'counts': 1}
            else:
                current[letter]['counts'] += 1
            current = current[letter]
            
    for word in words:
        current = trie
        for letter in word:
            if current['counts'] == 1:
                break
            else:
                current = current[letter]
            answer += 1
    return answer