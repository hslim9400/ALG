def solution(relation):
    answer = 0
    candidate_keys = {tuple(range(len(relation[0])))}

    def find_candidate(current_cols, target):  
        # 현재의 속성들 중 타겟 컬럼을 빼고 식별 가능성을 검증하는 함수
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
            if new_row in is_valid:  # 중복된다면 이 속성들로는 후보키가 될 수 없음
                return
            is_valid.add(new_row)
        else:  # 이 속성들로 식별 가능하다면
            candidate_keys.discard(tuple(prev_cols))  # 내 위의 컬럼집합은 나보다 속성을 하나 더 포함하므로 후보키가 되지 못한다.
            candidate_keys.add(new_cols)  # 그 대신 내가 새로운 후보키로 들어감
            for column in new_cols:
                find_candidate(list(new_cols), column)

    for column in range(len(relation[0])):
        find_candidate(list(range(len(relation[0]))), column)

    answer = len(candidate_keys)
    return answer

