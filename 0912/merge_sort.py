def merge_sort(arr):
    n = len(arr)
    if n == 1:
        return arr

    left = arr[:n//2]
    right = arr[n//2:]
    print(left, right)
    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)
    print(sorted_left, sorted_right)

    sorted_arr = []
    while sorted_left or sorted_right:
        if sorted_left and sorted_right:
            if sorted_left[0] > sorted_right[0]:
                sorted_arr.append(sorted_right.pop(0))
            else:
                sorted_arr.append(sorted_left.pop(0))
        elif sorted_left:
            sorted_arr.extend(sorted_left)
            sorted_left = []
        else:
            sorted_arr.extend(sorted_right)
            sorted_right = []
    print(sorted_arr)
    print()
    return sorted_arr


merge_sort([4, 5, 3, 6, 2, 7, 8, 1])
