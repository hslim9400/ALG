def solution(words):
    answer = 0
    trie = {'counts': 0}  
    # 트라이라는 자료구조를 알고있다면 좋다.
    # abc, aaa, aba, bbb라는 단어들이 있다면
    # trie = {
    #   a: {a: {a}}, b: {a, b}}, 
    #   b: {b: {b}}
    # }
    # 뭐 이런 식이 될건데, 여기에 글자별로 counts를 넣어 개수를 세줄 예정
    for word in words:
        current = trie  
        # 트라이의 꼭대기
        # 단어들의 첫 글자를 키로 갖는다.
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