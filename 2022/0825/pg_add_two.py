def solution(numbers):
    answer = []
    num_set = set()
    for i in range(len(numbers)-1):
        for j in range(i+1, len(numbers)):
            num_set.add(numbers[i] + numbers[j])
    answer = sorted(list(num_set))
    print(answer)
    return answer
