
def quick_sort(array, start, end):
    # TC: O(n*log(n)), SC: O(n), unstable
    if start < end:
        q = partition(array, start, end)
        quick_sort(array, start, q-1)
        quick_sort(array, q+1, end)


def partition(array, start, end):
    pivot_key = array[end]
    i = start
    for j in range(start, end):
        if array[j] <= pivot_key:
            array[i], array[j] = array[j], array[i]
            i += 1

    array[i], array[end] = array[end], array[i]
    return i


if __name__ == "__main__":
    array = [30, 26, 1, 3, 2]
    print(f"Before quick sort array: {array}")
    quick_sort(array, 0, len(array)-1)
    print(f"After quick sort array: {array}")

    array = [-5, -2, 3, 26, 30]
    print(f"Before quick sort array: {array}")
    quick_sort(array, 0, len(array)-1)
    print(f"After quick sort array: {array}")
