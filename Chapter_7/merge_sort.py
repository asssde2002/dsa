
def merge_sort(array):
    # TC: O(n*log(n)), SC: O(n), stable
    if len(array) < 2:
        return array

    mid = len(array)//2
    return merge(merge_sort(array[:mid]), merge_sort(array[mid:]))


def merge(l_array, r_array):
    result = []
    i = 0
    j = 0
    while i < len(l_array) and j < len(r_array):
        if l_array[i] <= r_array[j]:
            result.append(l_array[i])
            i += 1
        else:
            result.append(r_array[j])
            j += 1

    if i < len(l_array):
        result += l_array[i:] 
    elif j < len(r_array):
        result += r_array[j:]

    return result


if __name__ == "__main__":
    array = [30, 26, 1, 3, 2]
    print(f"Before merge sort array: {array}")
    array = merge_sort(array)
    print(f"After merge sort array: {array}")
