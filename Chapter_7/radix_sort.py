from functools import reduce


def radix_sort(array):
    # TC: O(n), SC: O(n), stable
    times = len(str(max(array)))
    for t in range(times):
        buckets = [[] for _ in range(10)]
        for i in array:
            b = (i // 10**t) % 10
            buckets[b].append(i)

        array = list(reduce(lambda x, y: x+y, buckets, []))

    return array


if __name__ == "__main__":
    array = [30, 26, 1, 3, 2, 235, 100]
    print(f"Before radix sort array: {array}")
    array = radix_sort(array)
    print(f"After radix sort array: {array}")
