def binary_search(array, start, end, target):
    if start > end:
        return -1

    mid = (start+end)//2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, start, mid-1, target)
    else:
        return binary_search(array, mid+1, end, target)


def binary_search_iterative(array, start, end, target):
    while start <= end:
        mid = (start+end) >> 1
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    
    return -1


if __name__ == "__main__":
    array = [-14, -3, 0, 5, 10]
    target = 5
    index = binary_search(array, 0, len(array)-1, target)
    print(index)

    target = -1
    index = binary_search(array, 0, len(array)-1, target)
    print(index)

    target = 5
    index = binary_search_iterative(array, 0, len(array)-1, target)
    print(index)

    target = -1
    index = binary_search_iterative(array, 0, len(array)-1, target)
    print(index)
