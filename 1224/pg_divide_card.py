def solution(arrayA, arrayB):
    answers = []
    arrayA.sort()
    arrayB.sort()
    a_targets = []
    b_targets = []
    for i in range(1, 1 + int(max(arrayA[0], arrayB[0]) ** (1 / 2))):
        # A배열과 B배열의 가장 작은 수의 약수 모으기
        if not arrayA[0] % i:
            a_targets.append(i)
            if i != arrayA[0]//i:
                a_targets.append(arrayA[0]//i)
        if not arrayB[0] % i:
            b_targets.append(i)
            if i != arrayB[0]//i:
                b_targets.append(arrayB[0]//i)
    a_set = set()
    b_set = set()
    print(a_targets, b_targets)

    # 조건 1: 내 배열안에 있는 모든 수들의 약수인지
    for target in a_targets:
        for a in arrayA:
            if a % target:
                break
        else:
            a_set.add(target)
    for target in b_targets:
        for b in arrayB:
            if b % target:
                break
        else:
            b_set.add(target)

    # 조건 2: 반대 배열의 모든 수들의 약수가 아닌 수인지
    ans_set = set()
    for target in a_set:
        for b in arrayB:
            if not b % target:
                break
        else:
            ans_set.add(target)
    for target in b_set:
        for a in arrayA:
            if not a % target:
                break
        else:
            ans_set.add(target)

    # 정렬하여 최댓값 출력
    answers = list(ans_set)
    answers.sort(reverse=True)
    if not answers:
        answer = 0
    else:
        answer = answers[0]

    print(answer)
    return answer

solution([14, 35, 119], [18, 30, 102])