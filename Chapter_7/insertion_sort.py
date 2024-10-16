
def insertion_sort(array):
    # TC: O(n**2), SC: O(1), stable
    n = len(array)
    for i in range(1, n):
        insert(array, i)


def insert(array: list, index: int):
    key = array[index]
    while index > 0 and key < array[index-1]:
        array[index] = array[index-1]
        index -= 1
    array[index] = key


if __name__ == "__main__":
    array = [30, 26, 1, 3, 2]
    print(f"Before insertion sort array: {array}")
    insertion_sort(array)
    print(f"After insertion sort array: {array}")
