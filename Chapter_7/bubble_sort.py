
def bubble_sort(array):
    # TC: O(n**2), SC: O(1), stable
    n = len(array)
    for i in range(n-1, 0, -1):
        flag = False
        for j in range(0, i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                flag = True

        if flag is False:
            break


if __name__ == "__main__":
    array = [30, 26, 1, 3, 2]
    print(f"Before bubble sort array: {array}")
    bubble_sort(array)
    print(f"After bubble sort array: {array}")
