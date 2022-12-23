# 맨 뒤에서부터 봤을때 어디까지 중복이 있는가? 를 찾아야 한다.
# 모든 부분문자열을 해시로 저장하면 메모리제한에 걸리고,
# 매 시행마다 문자열을 새로 만들면 시간제한에 걸린다.

# 포인터를 R-1로 두고 하나씩 땡겨오면서 시행
# 겹치는 문자열이 있는 인덱스와, 그 인덱스에서 겹치는 문자열을 저장한다. 
# 다음 시행에서 문자열의 다음 글자를 더하고 중복되면 계속 보관, 겹치지 않으면 삭제
# 중복되는 문자열이 없을때 까지 반복한다.
R, C = map(int, input().split())
words = []
for i in range(R):
    words.append(input())

idxs = list(range(C))  # 겹치는 문자열이 있는 인덱스들을 모아놓은 리스트
# 처음엔 모두 확인할 것
ans = R-1
strings = {}  # 겹치는 문자열을 보관
# {인덱스 : 중복되는 문자열} 꼴의 딕셔너리 
while ans:
    new_strings = {}  # 새로운 strings를 만들기 위한 temp느낌
    for i in idxs:
        if strings:
            base = strings[i]  # 지금까지의 중복된 문자열
        else:
            base = ''  # 첫 시행일 경우
        if base+words[ans][i] in new_strings.keys():  
            # 한 글자를 더 해주고 중복이 있는지 확인
            new_strings[base+words[ans][i]].append(i)
        else:
            new_strings[base+words[ans][i]] = [i]
    idxs = []
    strings = {}
    for made_word in new_strings.keys():
        if len(new_strings[made_word]) > 1:  # 중복이 있는 문자열이 있다면
            idxs.extend(new_strings[made_word])  # 중복이 있는 인덱스도 넣고
            for idx in new_strings[made_word]:
                strings[idx] = made_word  # 중복이 있는 문자열도 넣는다.
    if not idxs:  # 중복되는 문자열이 없으면 끝
        break
    ans -= 1
print(ans)


