def quick_select(array, start, end, k):
    if start <= end:
        q = partition(array, start, end)
        if k == q:
            return array[q]
        elif k < q:
            return quick_select(array, start, q-1, k)
        else:
            return quick_select(array, q+1, end, k)


def partition(array, start, end):
    pk = array[end]
    i = start
    for j in range(start, end):
        if array[j] <= pk:
            array[i], array[j] = array[j], array[i]
            i += 1
    
    array[i], array[end] = array[end], array[i]
    return i



if __name__ == "__main__":
    array = [30, 26, 1, 3, 2]
    k = 2
    print(f"Before quick select array: {array}")
    val = quick_select(array, 0, len(array)-1, k)
    print(f"The k ({k+1}) smallest value: {val}")

    array = [-5, -2, 3, 26, 30]
    k = 1
    print(f"Before quick sort array: {array}")
    val = quick_select(array, 0, len(array)-1, k)
    print(f"The k ({k+1}) smallest value: {val}")

