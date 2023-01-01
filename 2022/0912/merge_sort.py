def merge_sort(arr):
    # arr이 정렬해야하는 목표 리스트
    # arr을 왼쪽과 오른쪽으로 나누어 각각 정렬한 후 병합하며 정렬
    n = len(arr)

    if n == 1:
        # 분할 정복 종료 조건. 더이상 나눌 수 없다면 그대로 반환하고 원소가 한개라면 당연히 정렬된 상태이다.
        return arr

    print(f'target: {arr}')
    left = arr[:n//2]
    right = arr[n//2:]
    # 분할. 반으로 똑 떼서 나눈다. 아직 정렬되지 않았으므로 이를 출력하면 아래와 같다.
    print(f'left: {left},  right: {right}')

    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)
    # 분할한 왼쪽, 오른쪽 리스트를 정렬하여 저장한다. 재귀함수임. 정렬된 리스트는 아래와 같이 출력된다.
    print(f'sorted left: {sorted_left}, sorted right: {sorted_right}')

    # 이제 정렬된 왼쪽, 오른쪽 리스트가 있으므로 아래 로직을 통해 병합하며 정렬한다.
    sorted_arr = []
    # 정렬된 리스트를 담을 공간
    while sorted_left or sorted_right:
        # 준비한 왼쪽과 오른쪽 리스트의 원소를 모두 사용할 때 까지 반복한다.
        if sorted_left and sorted_right:  # 양쪽 모두 원소가 존재할 경우
            if sorted_left[0] > sorted_right[0]:  # 대소비교하여 작은 것을 넣어준다.
                # 안정정렬하기 위해 같은 값이라면 왼쪽의 값을 넣는다.
                sorted_arr.append(sorted_right.pop(0))
            else:
                sorted_arr.append(sorted_left.pop(0))
        # 둘 중 한개의 리스트를 모두 소진했다면 남은 한쪽은 이미 정렬되어 있으므로 그대로 넣어준다.
        elif sorted_left:
            sorted_arr.extend(sorted_left)
            sorted_left = []
        else:
            sorted_arr.extend(sorted_right)
            sorted_right = []
    # 병합이 끝났고 왼쪽과 오른쪽은 빈 리스트가 된다. 정렬 완료된 리스트를 출력
    print(f'sorted target: {sorted_arr}')
    print()
    return sorted_arr


merge_sort([9, 8, 7, 6, 5, 4, 3, 2, 1])
