def solution(relation):
    answer = 0
    candidate_keys = {tuple(range(len(relation[0])))}

    def find_candidate(current_cols, target):
        nonlocal candidate_keys

        is_valid = set()
        prev_cols = current_cols[:]
        current_cols.remove(target)
        new_cols = tuple(current_cols)
        for row in relation:
            new_row = []
            for column in new_cols:
                new_row.append(row[column])
            new_row = tuple(new_row)
            if new_row in is_valid:
                return
            is_valid.add(new_row)
        else:
            candidate_keys.discard(tuple(prev_cols))
            candidate_keys.add(new_cols)
            print(new_cols)
            print()
            for column in new_cols:
                find_candidate(list(new_cols), column)

    for column in range(len(relation[0])):
        find_candidate(list(range(len(relation[0]))), column)

    answer = len(candidate_keys)
    return answer

print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))