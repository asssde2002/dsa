from typing import List


def binary_search(array, start, end):
    if start == end:
        return start

    mid = (start+end)//2
    if array[mid] > array[end]:
        return binary_search(array, mid+1, end)
    else:
        return binary_search(array, start, mid)


def get_rotation_nums(nums: List[int]) -> int:
    if not nums:
        return 0

    return binary_search(nums, 0, len(nums)-1)


if __name__ == "__main__":
    array = [5, 10, 0, 1, 3]
    rotation_nums = get_rotation_nums(array)
    print(rotation_nums)    # 2

    array = [3, 5, 10, 0, 1]
    rotation_nums = get_rotation_nums(array)
    print(rotation_nums)    # 3

    array = [0, 1, 3, 5, 10]
    rotation_nums = get_rotation_nums(array)
    print(rotation_nums)    # 0

    array = [1]
    rotation_nums = get_rotation_nums(array)
    print(rotation_nums)    # 0

    array = []
    rotation_nums = get_rotation_nums(array)
    print(rotation_nums)    # 0
