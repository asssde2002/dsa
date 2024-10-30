def lis(nums):
    # TC: O(n^2), SC: O(n)
    n = len(nums)
    lis = [1] * n
    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i]:
                lis[i] = max(lis[i], 1+lis[j])

    return max(lis)


def lis_binarysearch(nums):
    # TC: O(n*log(n)), SC: O(n)
    n = len(nums)
    lis = [1] * n
    res = [nums[0]]
    for i in range(1, n):
        if res[-1] < nums[i]:
            lis[i] = len(res)+1
            res.append(nums[i])
        else:
            left, right = 0, len(res)-1
            target = nums[i]
            while left < right:
                mid = (left+right)//2
                if res[mid] < target:
                    left = mid + 1
                else:
                    right = mid

            res[left] = target
            lis[i] = left+1
    
    return max(lis)     # len(res) is also the answer


if __name__ == "__main__":
    nums = [50, 3, 10, 12, 7]
    # Function call
    print("Length of LIS is:", lis(nums))
    print("Length of LIS (optimized) is:", lis_binarysearch(nums))

