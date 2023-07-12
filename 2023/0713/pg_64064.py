from itertools import permutations
def solution(user_id, banned_id):
    answer = set()
    for permutation in permutations(user_id, len(banned_id)):
        for i in range(len(permutation)):
            user, banned = permutation[i], banned_id[i]
            if len(user) == len(banned):
                for j in range(len(user)):
                    if user[j] == banned[j] or banned[j] == '*':
                        continue
                    break
                else:
                    continue
                break
            else:
                break
        else:
            answer.add(tuple(sorted(permutation)))
            
    return len(answer)