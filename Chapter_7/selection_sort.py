
def selection_sort(array):
    # TC: O(n**2), SC: O(1), unstable
    n = len(array)
    for i in range(n-1):
        index = i
        for j in range(i, n):
            if array[j] < array[index]:
                index = j

        if index != i:
            array[i], array[index] = array[index], array[i]


if __name__ == "__main__":
    array = [30, 26, 1, 3, 2]
    print(f"Before selection sort array: {array}")
    selection_sort(array)
    print(f"After selection sort array: {array}")
