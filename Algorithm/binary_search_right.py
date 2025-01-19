def binary_search_right(array, start, end, target):
    if start > end:
        return start

    mid = (start+end)//2
    if array[mid] > target:
        return binary_search_right(array, start, mid-1, target)
    else:
        return binary_search_right(array, mid+1, end, target)
    

def binary_search_right_iterator(array, start, end, target):
    while start <= end:
        mid = (start+end)//2
        if array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return start


if __name__ == "__main__":
    array = [-14, -3, 0, 5, 10]
    target = 5
    index = binary_search_right(array, 0, len(array)-1, target)
    print(index)    # 4

    target = -1
    index = binary_search_right(array, 0, len(array)-1, target)
    print(index)    # 2

    target = 5
    index = binary_search_right_iterator(array, 0, len(array)-1, target)
    print(index)    # 4

    target = -1
    index = binary_search_right_iterator(array, 0, len(array)-1, target)
    print(index)    # 2
