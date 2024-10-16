def count_sort(array):
    # TC: O(n), SC: O(n), stable
    max_val = max(array)
    buckets = [0 for _ in range(max_val+1)]
    for i in array:
        buckets[i] += 1

    array = []
    for i in range(len(buckets)):
        for _ in range(buckets[i]):
            array.append(i)
        
    return array


if __name__ == "__main__":
    array = [30, 26, 1, 3, 2, 235, 100]
    print(f"Before count sort array: {array}")
    array = count_sort(array)
    print(f"After count sort array: {array}")
