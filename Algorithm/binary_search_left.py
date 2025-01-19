def binary_search_left(array, start, end, target):
    if start > end:
        return start

    mid = (start+end)//2
    if array[mid] < target:
        return binary_search_left(array, mid+1, end, target)
    else:
        return binary_search_left(array, start, mid-1, target)


def binary_search_left_iterator(array, start, end, target):
    while start <= end:
        mid = (start+end)//2
        if array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return start
    

if __name__ == "__main__":
    array = [-14, -3, 0, 5, 10]
    target = 5
    index = binary_search_left(array, 0, len(array)-1, target)
    print(index)    # 3

    target = -1
    index = binary_search_left(array, 0, len(array)-1, target)
    print(index)    # 2

    array = [-14, -3, 0, 5, 10]
    target = 5
    index = binary_search_left_iterator(array, 0, len(array)-1, target)
    print(index)    # 3

    target = -1
    index = binary_search_left_iterator(array, 0, len(array)-1, target)
    print(index)    # 2
